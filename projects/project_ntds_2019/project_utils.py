import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import timeit

def col_json_to_dict(df, cols):
    "Transform the json values inside a column into list of dictionaries"
    transformed_df = df
    for col in cols:
        transformed_df = transformed_df.assign(**{col: df[col].apply(json.loads)})
    return transformed_df

def col_dict_to_set(df, col, key):
    "Create a set from the values of the dictionaries give a key"
    get_set = lambda dict_list: set([dict_.get(key) for dict_ in dict_list])
    return df.assign(**{col: df[col].apply(get_set)})

def col_filter_dict_with_vals(df, col, field, values):
    "Filter dictionaries with specific values from a column with lists of dictionaries"
    filter_dicts = lambda dict_list: [
        dict_ for dict_ in dict_list if dict_.get(field) in values
    ]
    return df.assign(**{col: df[col].apply(filter_dicts)})

def get_intersections_length_adj_mat(col):
    "Get the intersecction length of the set of each entry with the set of every other entry in the column"
    start = timeit.default_timer()
    adj = np.zeros((col.shape[0], col.shape[0]))
    for (i, set_row) in col.iteritems():
        for (j, set_col) in col.iteritems():
            try:
                adj[i, j] = len(set_row.intersection(set_col))
            except AttributeError:
                adj[i, j] = 0
    adj_diag = np.diag(np.diag(adj))
    adj = adj - adj_diag
    stop = timeit.default_timer()
    print("Time: ", stop - start)
    return adj

def get_unions_length_adj_mat(col):
    "Get the unions length of the set of each entry with the set of every other entry in the column"
    start = timeit.default_timer()
    adj = np.zeros((col.shape[0], col.shape[0]))
    for (i, set_row) in enumerate(col):
        for (j, set_col) in enumerate(col):
            try:
                adj[i, j] = len(set_row.union(set_col))
            except AttributeError:
                adj[i, j] = 0
    stop = timeit.default_timer()
    print("Time: ", stop - start)
    return adj

def get_json_keys_from_col(col):
    "Get keys from all json strings within a column"
    fields = set()
    col = col.apply(json.loads)
    col = col.dropna()
    not_dict_idx = []
    if len(col[0]) > 1:
        col = col.explode()
    for (i, row) in enumerate(col):
        try:
            fields = fields.union(set(row.keys()))
        except AttributeError:
            not_dict_idx.append(i)
    return list(fields), not_dict_idx

def get_json_values_from_col(col, field):
    "Get values from all json strings within a column"
    field_values = set()
    col = col.apply(json.loads)
    col = col.dropna()
    not_val_idx = []
    if len(col[0]) > 1:
        col = col.explode()
    for (i, row) in enumerate(col):
        try:
            field_values.add(row[field])
        except (AttributeError, TypeError):
            not_val_idx.append(i)
    return list(field_values), not_val_idx

def sparsify_mat(mat,epsilon):
    "Set the values below a threshold to 0"
    return np.where(mat<=epsilon,0,mat)

def log10_transform(epsilon):
    "Return a lambda function to perform a log transform"
    return lambda x: np.log10(x+epsilon)

def plot_hist(col,title,xlabel,ylabel,log = False, figsize = (10,5), xticks_step = 1.0 , bins = 200, epsilon = 1e-6):
    "Plot a histogram of the column values"
    if log:
        col = col.apply(log10_transform(epsilon)) 
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(np.arange(min(col), max(col)+xticks_step,xticks_step))
    col.hist(ax = ax, figsize = figsize, bins = bins, color="teal")
    plt.close()
    return fig

def normalize_vote_rating(
    vote_rating_col,
    vote_count_col,
    names=["vote_average", "vote_count"],
):
    "Normalize vote rating using vote count according to IMDbs formula"
    c = vote_rating_col.mean()
    m = vote_count_col.min()
    vote_df = pd.concat([vote_rating_col, vote_count_col], axis=1, names=names)
    normalize_vote_rating = (
        lambda row: (row[names[1]] / (row[names[1]] + m)) * row[names[0]] + (m / (row[names[1]] + m)) * c
    )
    return vote_df.apply(normalize_vote_rating,axis=1)