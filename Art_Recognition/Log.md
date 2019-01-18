# Log Version 14

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
  * [Using Google Datalab and BigQuery for Image Classification comparison](https://medium.com/google-cloud/using-google-datalab-and-bigquery-for-image-classification-comparison-13b2ffb26e67)
  * [Jupyter Notebook in GCP](https://towardsdatascience.com/running-jupyter-notebook-in-google-cloud-platform-in-15-min-61e16da34d52)

**Thoughts** Ben's going to talk to his father, who has access to resources that we might need. Also, I am going to work on a much smaller dataset at first simply because it would be quicker to produce results to see what goes wrong.

**Things To Do**

  * Check out this [article](https://www.analyticsvidhya.com/blog/2018/06/unsupervised-deep-learning-computer-vision/).
  * Check this out too [Image Similarity With Deep Ranking](https://medium.com/@akarshzingade/image-similarity-using-deep-ranking-c1bd83855978)

## January 11, 2019

**Today's Progress** 

1. Created a quick and dirty model for clustering.
  * I did some brief visualization (see the frequencies of each class and took a peak at the images)
  * Removed bad/ corrupted files (the dataset has corrupted files, not sure why. But I'm pretty sure the pictures have already been corrupted, and not just corrupted on my computer)
  * Wrote a brief script that extracts the style layers. Not sure what to do with this because the styles are of different tensors (since VGG19 decreases the number of dimensions as layers approach the top).

## January 12, 2019

**Today's Progress** 

1. Tried Mini-batch. This is just a base model, and not actually intended to be used. Not even sure how to interpret the results. I may have to rethink the clustering method, simply because I'm not familar with it. I've decided to take a step back and do more research. It may be smarter to replicate what already exists.
  * I keep recieving this warning:
    > "/Users/jinli/anaconda3/lib/python3.6/site-packages/PIL/TiffImagePlugin.py:763: UserWarning: Possibly corrupt EXIF data.  Expecting to read 1311848 bytes but only got 785. Skipping tag 0" Skipping tag %s" % (size, len(data), tag))"
  * Not sure why, and the PIL library is poorly documented.
  * Yet it doesn't seem as if there's any problem, since I was still able to get the tensor representation, and the code still ran.

2. Looked Into Incremental PCA, very useful for online learning [source](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html), as I can reduce the dimensions of the images while keeping high variance.

3. Looked into many other clustering methods, but found that sklearn only supports two online learning clustering algorithms (has partial_fit). The first one is mini-batch k-means, second one is [Birch clustering method](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch). This method is scalable for large datasets, but not by number of features, so it would not be useful for hundreds of thousands of images.
   * Basic recap of Birch method:
   > " It constructs a tree data structure with the cluster centroids being read off the leaf." 
   * [Here](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#sphx-glr-auto-examples-cluster-plot-birch-vs-minibatchkmeans-py) for comparison between Birch and mini-batch k-means.

4. Checked out feature extraction from [sklearn](https://scikit-learn.org/0.15/modules/feature_extraction.html#feature-extraction). Most important thing to look at is the image feature extraction at the very end. Patch extraction may end up being useful, and graph connectivity for image segmentation may end up being used.

5. Did research on artistic styles. [Source I Used](https://artlandapp.com/art-movements-and-styles/) For examples of images, check out the link.

  * Abstract Expressionism
    * Postwar American paintings.
    * Also includes sculptures.
    * Dynamic art with "sweeping brushstrokes", dripping, and spilling.
  * Art Nouveau
    * 1890-1910
    * European 
    * Artwork has many curves, assymetrical lines.
    * Based on organic forms.
  * Avant-garde
    * Innovative art
    * Not specific
  * Baroque
    * dramatic motion
    * wants to produce drama, tension, grandeur
  * Classicism
    * focus on elegance and symmetry
  * Conceptual art
    * ideas and theoretical practices rather than visual forms
  * Constructivism
    * 1915
    * geometrically composed
  * Cubism
    * 1907
    * challenged traditional representations of forms
  * Expressionism
    * prioritized emotional experiences rather than reality
    * distortion, exaggeration, fantasy, dynamic
  * Fauvism
    * strong, vibrant colors
    * bold brushstrokes
  * Impressionism
    * thin, visible brushstrokes
    * emphasized movement and changing qualities of light
  * Minimalism
    * simple geometric shapes
  * Pop art
    * popular imagery
  * Rococo
    * elaborate ornamention
    * sensual 
  * Surrealism
    * 1924
    * channels irrationality 

**Thoughts**

1. I'm having doubts about clustering algorithms, simply because I'm not familar with the math behind the algorithms. 
2. But finding good and labeled art datasets may be difficult. A lot of datasets are partially labeled, and it might be interesting to use autoencoders to make use of the unlabeled dataset, though I know autoencoders have been considered a failure in the industry. 
3. Great News: I got access to the BAM dataset.


**Things To Do** 

1. Check out [Restricted Boltzmann Machine](https://skymind.ai/wiki/restricted-boltzmann-machine) and Deep Belief networks. Low priority since these are outdated methods. 
  * [Sklearn](https://scikit-learn.org/stable/modules/neural_networks_unsupervised.html) implementation.

2. Read ALOT more literature.


## January 13, 2019

**Today's Progress** 

1. Read this paper: [Recognizing Art Style Automatically in painting with deep learning](https://www.lamsade.dauphine.fr/~bnegrevergne/webpage/documents/2017_rasta.pdf). Notes:
  * Used the Wikipaintings dataset, Residual Neural Networks, 
  * Network is pretrained on AlexNet and ResNet, retrained for artistic style.
  * They showed that style learned from this dataset are consistent with styles from another dataset (ErgSap dataset). To make sure images don't overlap (a painting appearing in both datasets), they compared the metadata and removed paintings if the metadata matched.
  * Part of their model was based off of Gatys neural style transfer, which is something that I've replicated before. But one thing to note is that in this paper, the authors used the content to help predict style.
    > "a person is more likely to appear in an impressionist painting than in an abstract painting"
  * Styles That They Used: 
    > "Abstract Art, Abstract Expressionism, Art Informel, Art Nouveau (Modern), Baroque, Color Field Painting, Cubism, Early Renaissance, Expressionism, High Renaissance, Impressionism, Magic Realism, Mannerism (Late Renaissance), Minimalism, Naive Art (Primitivism), Neoclassicism, Northern Renaissance, Pop Art, PostImpressionism, Realism, Rococo, Romanticism, Surrealism, Symbolism and Ukiyo-e."
  * Used the bagging technique (average the output of different predictions on variations of the input). The variation they used was flipping the picture horizontally.
  * Data Augmentation Methods: 
    > "random, horizontal flips, rotations, axial translations and zooming"

2. Read this paper: [How the Arts Impact Communities](https://www.princeton.edu/~artspol/workpap/WP20%20-%20Guetzkow.pdf)
  * art revitalizes neighborhoods and promote economic prosperity
  * art increases community cohesion
  * creates social capital (just like the statements in scenesbook)
  * art attracts tourists, businesses, investments
  * art improves individual health, psychological well-being

3. Looked through the art institute of chicago to see the types of imagery that are represented.
4. Skimmed these papers (didn't feel that they were worth reading):
  * [Rating Image Aesthetics Using Deep Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7243357)
    1. Basically tried to estimate how aesthetic an image is through style.
    2. Not really related to art, but pretty interesting and has quite a few citations.
  * [Image Style Classification based on Learnt Deep Correlation Features](https://www.cs.ccu.edu.tw/~wtchu/papers/2018TMM-chu.pdf). 
    1. Correlate different features to predict style
    2. Math oriented, but willing to reread this paper when I've decide to start thinking about the intricacies of the model.

4. So I've got access to the [BAM dataset](https://bam-dataset.org/).
  * They made me do some manual classification

**Thoughts** 

1. I've decided that we should not do unsupervised learning.

Reasons why:
  * I've tried kmeans clustering algorithm, and I do not feel that it is reliable. First, metrics that measure the success of clustering algorithms does not tell me anything meaningful about why images are grouped in a certain way. Second, clustering algorithms focus too much on what the image actually is rather than the style. I tried extracting lower layers, but this makes the process really slow, as the lower layers have huge number of filters.
  * Most clustering algorithms do not scale very well with large datasets. According to sklearn documentation, the only two clustering algorithms that scale well are k means and Birch, and Birch does not scale well with number of features.
  * Most clustering algorithms are not online, which is a problem because it is a very bad idea to load the entire dataset into memory. That leaves me with only one option in sklearn: mini-batch k-means. This is a problem because my options are so limited.
  * Even after clustering, we have to do a lot more manual labor trying to understand why the algorithm clustered certain images together. Sklearn does explicitly support this kind of analysis for images (sklearn only really provides metrics on measuring the clustering algorithm, which is completely meaningless to understanding why images are clustered the way they are.) If we had to understand the clustering model, every time we make even a certain change (like changing a hyperparameter), we would have to manually analyze with our eyes why certain images cluster together.

2. Different datasets dramatically impact the image classifications. There's no way we can apply data from a set with only paintings to the real world because the real world contains other different types of art. What I think we need to do is first classify the type of artwork first (is it a painting, sculpture, watercolor, pencil sketch, 3D graphic.) 
  * If we know it is not a painting, then there's no need to apply classification to see whether the style is impressionism, surrealism, etc. 
  * If it is a painting, then apply the style classification.

3. Style is not the only thing that defines a community. 
  * It would be interesting to look at mood of a painting (gloomy, peaceful, happy, scary).
  * Maybe also classifying content may say something the community, but we would have to deal with a lot more classes. Also, we would need to do more complicated image recognition (like applying YOLO algorithms to find all objects in an image), which would take more learning and research (since I'm not familar with YOLO).


## January 14, 2019

**Today's Progress** 

1. Spent an hour talking to Ben, where I described how a CNN works, and how we are going to build two classifiers. I also briefed Ben about how in the long run, Google Cloud is not a smart option simply because we will be running CNNs with millions of parameters, and it would be much better to build our own machine learning computer. I also talked to him about the datasets that we plan to use.

2. Reread this research paper from [BAM](https://arxiv.org/pdf/1704.08614.pdf)
  * they used the dataset of photos collected from Behance, a website that contains millions of artistic items from modern artists
  * artistic content spans from fine art to technical drawings to graphitti.
  * precision of their hand labels is 90%
  * check out related works (not focusing on that right now)
  * Media attributes:
    * 3D computer graphics
    * comics
    * oil painting
    * pen ink
    * pencil
    * sketches
    * vector art
    * watercolor
  * These categories were chosen mainly because they were easily distinguishable from one another.
  * Emotion attributes
    * calm/peaceful
    * happy/cheerful
    * sad/gloomy
    * scary/fearful
  * Paper also described the annotation pipeline, but I skimmed that part.
  * Found that object detection in photographs do not perform as well when classifying art images
    * but we are not doing object detection, so this doesn't really matter for us
  * it's important for us to be able to validate our trained model with an outside dataset
  * the more classes of output, the trickier it is to train a model that excels at classifying all the classes


## January 15, 2019

**Today's Progress** 

1. Tried to learn sql with python. Got things running and fiddled around with the dataset.
2. Wrote up my game plan for training our model. Check it out [here](https://github.com/JinLi711/UIA/tree/master/Art_Recognition/medium_classification).


## January 17, 2019

**Today's Progress** 

1. Talked to the RCC about the computing center.
  * They told me to make an general account under Professor Terry Clark.
  * For computing, I would probably need 2 GPUs (Nvidia). But I could also work with a cluster of cpus. Not sure what I need yet.
    * The person I talked to said I probably shouldn't use more than 2 GPUs because GPUs are high in demand right now.
  * To make sure my script runs in parallel, I should send my code to rcc so they could optimize the code for running tensorflow on the gpus.
  * I also think python notebooks would not work, so we need to build a script (though it would be a good idea to start with a python notebook, but transfer everything to a script when we are done.) 
    * Also, create a bash script for executing the python script.

2. Spent some time skyping with Ben to talk about how to best communicate our ideas and our plans.
  * Ben's going to finish the write up
  * I'm going start step 1 of the process. 

3. Email About Murals:
  * Hyesun
    > Hello, all I want to share three different types of murals that possibly link with cafe as reference. 
    > 1. Traditional / neighborly/local type mural I was looking at the Englewood street view on Google map, and wondering about the artist. He is native Chicago born in South Side, and he produced more than 400 murals in Chicago and other cities. If you go to this website in mural portfolio section, you can see all murals and their address. I just found there are many of his murals in Hyde Park too! http://www.statikone.net/ARTIST_MISSION.html  We talked about Mexican/ African mural today in the meeting. These murals express humor, satire, political message mixed with heritage of their root too. These murals show more characteristics of ethnicity?

    > 2. Corporate/utilitarian type mural This is Wabash Arts Corridor initiative launched by Columbia College.These works started in Wabash Avenue near South Loop, then now expanding to north side as well. This type presents more art itself as part of street decoration and revitalization project. You can find they are inspirations from geometries, animals, flowers, and nature in different colors and shapes. There is not much link to ethnicity in this type, maybe few. http://wabashartscorridor.org/project/

    > 3. Bohemian type mural I see Wicker Park as an example of murals in bohemian neighborhood. If you see them on this website, there are more likely to be comic or cartoons that convey the idea of “diversity.” They show ethnic diversity or LGBT artistic way, by drawing variation of colors, faces, sign of “love for everyone”, “we all live here”, and signs in Chinese character as well. There is commonality between this type and traditional/neighborly type of mural in that they convey some message on social justice and equality, although traditional one has more linked to cultural heritage. What do you think http://www.wickerparkbucktown.com/muralspublicwork/

    > I am trying to connect the characteristic of street art to three types of neighborhood which I think is possibly useful for case study of cafes too. Can we possibly characterize music in cafe as well? which is a question to find out together. 
  * Alexis
    > I looked at all the links that you sent. What you found was very interesting because I found very interesting difference in the type of art that is seen in the neighborhoods.  I noticed that the type of art that is in the neighborhoods you have identified as Bohemian leans more into the arena of pop art, graffiti art, & socially criticizing art. It is telling a story about the area and/or being used to claim the area and give it character, the character that the neighborhood holds.  The art used bright colors and the images were identifiable but mostly cartoon based. 

    > Within the corporate neighborhoods I noticed the art was very geometrical, abstract, and/or seemed to serve the sole purpose of being ascetically pleasing. Within the neighborhoods you have as neighborly or traditionally, I noticed that this art had a reclamation and pride vibe. It seems to serve the purpose of claiming a culture and people and portraying those people and culture in positive light. This art focused a lot on telling the story of black history or focusing on famous and prominent members of the black community like the Obama family. 

    > I feel that what you have found really does highlight how the art is used for different reasons or serves different purposes in different communities.

    > I feel that these characteristics of the art in each community may translate into the type of patrons of the cafes and the music played in the cafes.  For example using these characteristics in art, I would be curious to observe it in the neighborly communities (specifically black) if their cafe's played more neo-soul, r&b, or contemporary/brass jazz music or if in the corporate if they played more Kenny G (elevator jazz) or pop music or if the Bohemian neighborhoods played more contemporary jazz rap, contemporary neo-soul r&b (like jorga smith). 

    > These are just my thoughts. 

  
  * My Thoughts
    * I need to be able to fit into this conversion in trying to classify images into different styles to say something about the communities. However, the conversation seems to be about murals, not just any artwork. That means I need to find a dataset that only contains murals and are labeled by the mural's style. Technically I can use the dataset I have now, but it might not generalize well.
    * I really don't want to label images by hand for the training set, but I would consider it. Or maybe hire someone else to label these images (not sure).
    * Hyesun wants us to classify emotions (humor, satire, political messages). I don't think that's possible to do with CNNs. 
      * Maybe humor, but definitely not satire or political messages. 
      * That's simply because satire and political messages require domain knowledge beyond whats in the image.
      * Maybe classifying other emotions are possible. However, this is low priority.
    * It might be possible to classify graphitti art. I'm sure there's a dataset on graphitti.
        
3. Researched emotion types.
  1. Robert Plutchik's theory
    * The circumplex as a general model of the structure of emotions and personality. [Source](https://psycnet.apa.org/record/1997-97129-001)
    * Emotions:
      * Fear, frightened, scared.
      * Anger, rage
      * Sadness, sorrow, grief
      * Joy, happy, gladness
      * Disgust 
      * Surprise
      * Trust
      * Anticipation
    * Fear, anger, sadness, joy, disgust would be doable in image classifications.

  2.  