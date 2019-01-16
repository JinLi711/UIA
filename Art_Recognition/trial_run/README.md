# Trial Run

Learning google cloud platform would be a small distraction right now (I don't even know how to use SQL :sad:), and I need to get the ball rolling to show that we can have something interesting. So I've decided to do a test run with a significantly smaller dataset.

## Data Set

[Source](https://www.kaggle.com/thedownhill/art-images-drawings-painting-sculpture-engraving)

Summary: 9000 images with 5 types of art.

Drawings and watercolours
Works of painting
Sculpture
Graphic Art
Iconography (old Russian art)

## What we want to do

We want to create a semi-supervised algorithm to sort images (we will only use some of the labels). We want to see how well the unsupervised algorithm works by comparing the clustering with the labels. This is helpful:[K Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)

## Plan

1. Load the data
 1. Create a function that loads image files batches at a time (can't load everything to memory)
2. Preprocess the data
 1. Resize the images to a certain size.
 2. PCA dimension reduction.
2. Preprocess Plan 2 (going with this one first)
 1. Run images through VGG19, extract lower layer activations.
 2. Create a class with attributes image name, category, tensor of the layers.
3. Try different algorithms
 1. K means

## Sites to check out

1. [Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py)

## Notes

### K-Means

[Source](https://scikit-learn.org/stable/modules/clustering.html#k-means)

  * Need number of clusters to be specified.
  * scales well to large number of samples
  * Basically randomly assign items into different categories, calculate the mean in each category, and then for each item, move that item to the category where the difference between the value of the item and the mean of that category is the lowest.
  * Assumptions: clusters are convex (not sure if the clustering for my data set would be convex)
  * bad for elongated clusters and irregular shapes
  * should run PCA before hand (to reduce curse of dimensionality and speed up computation)
  * objective func will always converge, though not always to the global minimum

### Mini-batch K-Means

  * computational time is lower


# Decision

After this initial exploration and talking to Ben, we decided that it is best NOT to do unsupervised learning. We will do supervised instead. I explained my reasoning in the Log.
