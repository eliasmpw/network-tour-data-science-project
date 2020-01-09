# Actors Tour of Data Science - Final Project

## Overview

The aim of the project is to estimate and predict quantities related to the perception of the audience related to a movie with respect to the actors, i.e. the hiring cost of an actor. This will be done using graph theory and techniques learned in the EE-558 course in EPFL.

## Structure
```
├── data                                    <- Directory containing the datasets and the GEFX files for the Gephi visualizations.
    └── initial_graph.gexf                  <- GEFX file for the initial graph built. 
    └── louvain_graph.gexf                  <- GEFX file for the generated communities classification.
    └── tmdb_5000_credits.csv               <- Dataset from Kaggle containing actor, director and crew credits for movies.
    └── tmdb_5000_movies.csv                <- Dataset from Kaggle containing information about movies, like revenue, budget and rating.
├── plots                                   <- Directory containing the generated plots
    └── adj_actors_heatmap.pdf              <- Heatmap of actors adjacency
    └── both_spectrum.pdf                   <- Plot of laplacian spectrum
    └── both_spectrum.png                   <- Plot of laplacian spectrum
    ...
    ...
    └── vote_signal_tikhonov.pdf            <- Plot of regularized vote values
    └── votes_count_hist.pdf                <- Histogram of vote count average
    └── votes_hist.pdf                      <- Histogram of vote value average
├── 00_build_actor_dataframe.ipynb          <- Data cleaning
├── 01_explore_data.ipynb                   <- Some statistical analysis of dataset
├── 02_build_actors_graph.ipynb             <- Creating the network/graph
├── 03_analyze_graph.ipynb                  <- Graph analysis
├── 04_type_graph_prop_nodes.ipynb          <- Node properties analysis
├── 05_analysis_and_visualization.ipynb     <- Community creation and visualization
├── 06_Vanilla_Linear_Reg.ipynb             <- Prediction of popularity, revenue and budget
├── 07_tikhonov_reg.ipynb                   <- Prediction using a Tikhonov regularized dataset.
├── 08_filters.ipynb                        <- Creating LP, HP, BP and Thikhonov filters and using them for prediction
├── project_utils.py                        <- Utility functions used in the notebooks

```

## Setup

For a local installation, you will need [git], [Python], and packages from the [Python scientific stack][scipy].
If you don't know how to install those on your platform, we recommend to install [Miniconda] or [Anaconda], a distribution of the [conda] package and environment manager.
Follow the below instructions to install it and create an environment for the course.

1. Download the Python 3.x installer for Windows, macOS, or Linux from <https://conda.io/miniconda.html> and install with default settings.
   Skip this step if you have conda already installed (from [Miniconda] or [Anaconda]).
   * Windows: double-click on `Miniconda3-latest-Windows-x86_64.exe`.
   * macOS: double-click on `Miniconda3-latest-MacOSX-x86_64.pkg` or run `bash Miniconda3-latest-MacOSX-x86_64.sh` in a terminal.
   * Linux: run `bash Miniconda3-latest-Linux-x86_64.sh` in a terminal or use your package manager.
1. Open a terminal.
   Windows: open the Anaconda Prompt from the Start menu.
1. Install git with `conda install git`.
1. Navigate to the folder where you want to store the course material with `cd path/to/folder`.
1. Download this repository with `git clone https://github.com/eliasmpw/EE-558-ntds`.
1. Create an environment with the packages required for the project with `conda env create -f environment.yml`.

## Running
To run the notebooks, do the following:

1. Open a terminal.
   Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate ntds_2019`.
1. Navigate to the folder where you stored the course material `cd path/to/folder`.
1. Start Jupyter with `jupyter lab`.
   The command should open a new tab in your web browser.
1. In your browser, open and run the notebooks that have a number in their name, in the order specified by the numbers. 
e.g. 00_build_actor_dataframe.ipynb, then 01_explore_data.ipynb, then 02_build_actors_graph.ipynb, etc.
1. Once done, you can run `conda deactivate` to leave the `ntds_2019` environment.

## Authors
- Andres Ivan Montero Cassab
- Ariel Hugo Alba Rios
- Elias Manuel Poroma Wiri
- Adrian Gabriel Villarroel Navia

