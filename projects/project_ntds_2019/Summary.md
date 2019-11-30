# Neighborhood of Actors, Who is the MVP among them?

### Team 8 - Network Tour of Data Science

### 1. Story

The idea of the project is to find if there exist a community of actors, how
they relate among them and who are the most popular actors.

For this purpose the dataset of IMDB will be used, this dataset is downloaded
from kaggle :... PUT LINK HERE

The tools that we are going to use for this project are: Pandas, Scikit-learn,
Networkx, Matplotlib, and others.

### 2. Acquisition

The data consisted of : ... description of the data

For the creation of the graph we did this ...

### 3. Exploration

The first exploration that we did show the following:

- #### Connected components:
  Number of connected components 2, however we decided to sparsifiy more the
  matrix so that is manageable and feasible to use, obtained one connected
  component
- #### Sparisty of the graph:
  INSERT PLOT HERE
- #### Diameter:
  4, meaning that any actor is 4 steps away of knowing any other actor.
- #### Degree distribution:
  INSERT PLOT HERE
- #### Spectrum:
  INSERT PLOT HERE
- #### Type of graph:
  The network is a small world, to get this assumption a similar generated
  Erdős–Rényi network was created and network statistics like clustering
  coefficient and the mean shortest path were found for both. Mean shortest path
  is the same, however, clustering coefficient is different.  
  Small networks should have some spatial structure, that is reflected on a
  bigger clustering coefficient.
- #### Properties of the nodes:

  - Average Degree: 590.388635210553
  - Average clustering coefficient: 0.6403268534042411
  - Nodes with higher centrality:

    - Britney Spears - 0.7812182741116752
    - Melissa Joan Hart - 0.7578680203045686
    - Orlando Jones - 0.733502538071066
    - Nicholas Rowe - 0.7324873096446701
    - Tom Selleck - 0.7279187817258883

  - Nodes with small centrality:

    - Ben Youcef 0.0040609137055837565
    - Caitlin Fitzgerald 0.003553299492385787
    - Kirby Heyborne 0.0015228426395939086
    - J.D. Williams 0.0010152284263959391
    - Toshirō Mifune 0.0010152284263959391

  - Hub Nodes (Just some actors, because number of hubs is 964):

    - 50 Cent
    - AJ Michalka
    - Aaron Abrams
    - Aaron Stanford
    - Aasheekaa Bathija
    - Zhang Ziyi
    - Zoe Kazan
    - Zoe Lister-Jones
    - Zoe Saldana
    - Zooey Deschanel

* #### Analysis of the attributes:
* #### A visualization of the network: I did a simple plot, for this, if elias can improve insert the improved picture here
* #### A reflection on the insights

### 4. Exploitation

- Clustering: Spectral clustering findings
- Critical evaluation of the results
