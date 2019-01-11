# Log Version 3

This is a log of all the progress made for the art recognition project.

## January 5, 2019

**Today's Progress**

1. Discussed with Ben and Michal about our objectives and plans.
  * We discussed possibilities of scraping artworks from Wikipedia or [MoMa](https://www.moma.org/collection/?fbclid=IwAR2YrXrfWNHidoUsCB86_s_C28h-_NnxOsggwxTO5WeJkHBrSbw_FR4cbak)
  * We decided that machine learning (more specifically semi-supervised deep learning with convolutional neural network) would be the best way to approach our goals.
  * However, we can also frame this problem as a unsupervised deep learning.
  * We wanted to answer questions like:  
    Do certain neighborhoods have preferences?  
    Do they favor certain types of art?  
    How are we going to categorize the art in a neighborhood?  
    How can we classify pictures we might pull from instagram into categories that we can then use to look at neighborhoods preferences for particular types of visual art? 
  * We discussed how we can compare style of images by comparing the lower layers of cnns and finding a metric to measure mathematically defined style. Like what I did [here](https://github.com/JinLi711/Neural-Style-Transfer)  
  * Discussed how we can leverage resources like the supercomputer at Midway.  

2. Found existing datasets we could use.

**Thoughts** It is important to note that me and Ben have different objectives from Michal. Whereas Michal wants to create an app of some sort to be able to recognize artworks after taking a picture, me and Ben want to analyze how distributions of artwork types vary from location to another.

**Thoughts** There probably is not a need to scrape because there are datasets out there that we can use for free.

**Things To Do** 

1. Prepare for meeting with Ben at 4:45 p.m. Monday at the Regenstein Library.
2. Find and explore resources that we can leverage. Jot notes down.

## January 6, 2019

**Today's Progress**

1. Added onto the [resources page](https://github.com/JinLi711/UIA/blob/master/Art_Recognition/Resources.md).
2. Read up on clustering algorithms.
  * Source: [Introduction To Clustering Algorithms](https://medium.freecodecamp.org/how-machines-make-sense-of-big-data-an-introduction-to-clustering-algorithms-4bd97d4fbaba)
  * K-Means Clustering. Basically randomly assign items into different categories, calculate the mean in each category, and then for each item, move that item to the category where the difference between the value of the item and the mean of that category is the lowerst. One variation of this is to randomly assign one item to one group, and then start assigning the other items to the groups. But note that we need to know the categories before hand.
  * Hierarchical Clustering. Create a distance matrix. Pair the observations with lowest distance. Repeat. End up with an heirchal structure.
  * Graph Community Detection. Skimmed it since it's not incredibly important for what we are trying to accomplish.
  * [Edge-Betweenness.](https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm) Start with all vertices grouped in one giant cluster. Then iteratively removes least important edges, producing a hierarchal structure.
  * [Clique Percolation.](https://en.wikipedia.org/wiki/Clique_percolation_method) 
  * [Spectral clustering](https://en.wikipedia.org/wiki/Spectral_clustering)

3. Took a look at [OpenCV](https://opencv.org/). This is not used for training (we use keras or tensorflow for that) but more for analyzing the results of the training.

**Thoughts** OpenCV might not support Keras (not sure)


## January 7, 2019

**Today's Progress** 

1. Spent almost two hours talking to Ben about our objectives and plans.

2. Looked up different clustering algorithms metrics
  * [Silhouette Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
  * [Homogeneity, completeness and V-measure](https://scikit-learn.org/stable/modules/clustering.html#homogeneity-completeness-and-v-measure)
  * [Calinski-Harabaz Index](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabaz-index)  

## January 9, 2019

**Today's Progress** 

1. Spent some time discussing possible clustering algorithms and metrics.

2. Read this research [paper](https://arxiv.org/abs/1704.08614). This paper is quite relevant since it discusses using a semilabeled dataset to classify both style and mood. It also explains the BAM dataset, which might be a good alternative since it focuses on comtemporary art.

**Things To Do** 

1. Get Google Cloud started. Start training.

## January 10, 2019

**Today's Progress** 

1. Learned how to use Google Cloud and helped Ben set up Google Cloud.

**Thoughts** Ben's going to talk to his father, who has access to resources that we might need. Also, I am going to work on a much smaller dataset at first simply because it would be quicker to produce results to see what goes wrong.
