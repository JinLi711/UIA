# Log Version 34

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
    * Also, create a [bash script](https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php) for executing the python script.

2. Spent some time skyping with Ben to talk about how to best communicate our ideas and our plans.
  * Ben's going to finish the write up.
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
  
  * Hyesun
    >Thanks for reaction. Definitely! I think we can sharpen this idea further and build some method to match types of murals and musics with types of cafe.

    > There are cafes in Bronzeville (categorized as neighborly/local/traditional) we can take a look more closely for this type.
      1. Sip & Savor cafe: 528 E 43rd St, Chicago, 60653
      2. Ain’t She Sweet cafe: 2920, 526 E 43rd St, Chicago, 60653

    > They actually locate next to each other on 43rd St as business neighbors.  When you look at their phots on Yelp or Google map, they take are proactive in exhibiting local art paintings in their interior space. It’s very similar style that we see on the murals in this neighborhood. Also, they promote them selves as third space. For example, Sip & Savor’s sleeve for coffee directly writes, “Sip & Savor- Where coffee and community meets.” 

    > What’s interesting is there used to be famous “Wall of Respect” mural next to these cafes. It was part of black art movement that thrived in 1960s-70s.
    > That mural was torn down after accidental fire on building in 1971, so it does not exist anymore as a vacant land now. https://en.wikipedia.org/wiki/Wall_of_Respect  

    > There are lots of churches on the 43rd street, and recently there are community art center and galleries built to revive art movement there. 
    > Thinking of history and what’s present now, I think cafe in zipcode 60653 can be interesting case study for neighborly type to incorporate street art (or other forms of art) and music. Visiting them and listening what music they play is one option, then we can also ask owner about more info.

    > We can apply same thing for cafe in Bohemian and Corporate type of neighborhood too - in conjunction of street art and music as sensory experience of cafe patrons.

    > These are images of presence of arts around two cafes in zip code 60653 below. You can look up their street view on Google.


  
  * My Thoughts
    * I need to be able to fit into this conversion in trying to classify images into different styles to say something about the communities. However, the conversation seems to be about murals, not just any artwork. That means I need to find a dataset that only contains murals and are labeled by the mural's style. Technically I can use the dataset I have now, but it might not generalize well.
    * I really don't want to label images by hand for the training set, but I would consider it. Or maybe hire someone else to label these images (not sure).
    * Hyesun wants us to classify emotions (humor, satire, political messages). I don't think that's possible to do with CNNs. 
      * Maybe humor, but definitely not satire or political messages. 
      * That's simply because satire and political messages require domain knowledge beyond whats in the image.
      * Maybe classifying other emotions are possible. However, this is low priority.
    * It might be possible to classify graphitti art. I'm sure there's a dataset on graphitti.
    * Future Project (maybe in a year or so): music classification.
      * Clark said in his meeting that he had a dataset of 20 million songs somewhere.
      * Paper to get started: [A Survey of Audio-Based Music Classification and Annotation](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5664796).
        
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

4. Looked over (skimmed abstract, conclusion) some of the literature on emotion recognition. Picked the ones that may be useful.
  * Most of the literature talks about facial emotional recognition.
  * Might be interesting to consider building a model (YOLO model) that can identify a picture of a face. Then run another model that identifies the emotion.
  * Good place to get started: [Real-time Convolutional Neural Networks for Emotion and Gender Classification](https://arxiv.org/pdf/1710.07557.pdf)
  * [Medium article](https://medium.com/dair-ai/detecting-emotions-with-cnn-fusion-models-b066944969c8) on combining image and text for emotion recognition
  * [Learning deep features for image emotion classification](https://ieeexplore.ieee.org/document/7351656)
  * [Learning Multi-level Deep Representations for Image Emotion Classification](https://arxiv.org/abs/1611.07145)
  * [A Mixed Bag of Emotions: Model, Predict, and Transfer Emotion Distributions](https://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Peng_A_Mixed_Bag_2015_CVPR_paper.html)
  * [Building Emotional Machines: Recognizing Image Emotions through Deep Neural Networks](https://arxiv.org/pdf/1705.07543.pdf)

5. Read up on some of the graphitti literature.
  * A decent amount of work has been done on video graphitti detection. We don't need something that advanced.
  * Should look this over again:
    * [Efficient Graffiti Image Retrieval](https://viscenter.uncc.edu/sites/viscenter.uncc.edu/files/CVC-UNCC-12-02.pdf).

6. Spent an hour talking to Alexis. She's going to write up what we talked about in her log.
  * Alexis going to try to search for categorical words and respond to her emails.
  * I'm going to try write up my game plan for approaching word categorization.

**Thoughts** This paper would be very useful to check out again: [Describing Artworks Using Convolutional Neural Networks](http://cs231n.stanford.edu/reports/2016/pdfs/200_Report.pdf).


## January 18, 2019

**Today's Progress** 

1. Spent some time understanding the SQL file and created a plan for how to grab the data.

2. Was able to some data wrangling and memory reduction on the SQL file. Was able to create 2 pickle files that contains the labels and the urls (the sql dataset was set up a bit awkwardly, so it took time to merge different parts of the dataset)

3. Created a scraper that is able to download images into the correct files. I had to be very meticulous about where I put the downloaded files.

## January 21, 2019

**Today's Progress** 

1. Did some more research on murals.
  * Definition of Mural: a painting or work of art that is created on a [wall](https://www.dictionary.com/browse/mural).
  * Although murals are not paintings, many murals have styles that are similar to the styles of paintings.
  * Looked through murals on [Pinterest](https://www.pinterest.com/herrsuite/murals-breathtaking-complex/).
    * Observations:
      1. Murals are painted on many places other than public walls. People have murals in their own home, on staircases There was even a mural on a car.
      2. Styles are very unobvious. It's very difficult for me personally to look at the murals and decide on the style of mural. 
  * Looked at public art in [Chicago](https://www.choosechicago.com/things-to-do/museums-and-arts/public-art/street-art-and-murals/).
    * Possible future problem: the pictures are not exactly on the image itself (the photos include other items not related to the mural)
  * [LA](https://www.muralconservancy.org/murals) has an amazing database on murals. I'm wondering if I could find something like this in Chicago.
  * Checked out the [Pilsen gallery](https://interactive.wttw.com/my-neighborhood/pilsen/murals)
    * Again, the murals are very diverse and styles are unobvious. 
  * Skimmed through this article on [Google Art Project](https://www.theguardian.com/artanddesign/2015/mar/27/google-street-art-project-mural-conservancy). Not really that useful.

2. Created the model, trained. Honestly wasn't even that bad (I just reused the model that I created in my CIFAR 100 project): 

| Layer (type)      |           Output Shape         |     Param #   |
|------------------- |------------------------------  |-----------------------------------
| input_7 (InputLayer)    |     (None, 128, 128, 3)    |   0         |
| conv2d_7 (Conv2D)        |    (None, 123, 123, 32)    |  3488      |
| max_pooling2d_19  | (MaxPooling (None, 62, 62, 32)     |   0         |
| batch_normalization_19 | (Batc (None, 62, 62, 32)     |   128     |  
| separable_conv2d_13  | (Separab (None, 60, 60, 64)     |    2400    |  
| max_pooling2d_20  | (MaxPooling (None, 30, 30, 64)  |      0         |
| batch_normalization_20  | (Batc (None, 30, 30, 64)     |   256       |
| separable_conv2d_14 | (Separab (None, 28, 28, 128)    |   8896      |
| max_pooling2d_21 | (MaxPooling (None, 14, 14, 128)    |   0         |
| batch_normalization_21 | (Batc (None, 14, 14, 128)     |   512       |
| flatten_7 (Flatten)    |      (None, 25088)      |       0        | 
| dense_7 (Dense)        |      (None, 128)         |      3211392   |
| Drop-Out (Dropout)    |       (None, 128)       |        0         |
| oil_paint (Dense)      |      (None, 3)           |      387    |   

  * Total params: 3,227,459
  * Trainable params: 3,227,011
  * Non-trainable params: 448

  * 69% validation accuracy, even though we only had about 500 pictures for the train set, and no pretrained model. Seems promising. (I trained on only the oil paintings, and the outputs were positive, negative, and unsure.) 
  * Baseline (always picking the most frequent class) is 51%.

## January 22, 2019

**Today's Progress** 

1. Read Ben's writeup/proposal for neural networks. See [here](https://github.com/JinLi711/UIA/tree/master/Art_Recognition/proposals).

## January 24, 2019

**Today's Progress** 

1. So me and Ben discussed what research we might need to be able to analyze pictures of art. One of the problems is that have to look at mural pictures that are taken that include other things other than the mural. For example, some pictures contains the scenary around the mural.
   * Ben is going to look at image processing for the pure image (just the mural), and I want to look at image processing for the "full image" (picture containing the scenery.)
   * My thoughts on how to approach this:
     * Murals have very distinct style from real life imagery. For example:
     ![alt Mural](https://static1.squarespace.com/static/57615c85356fb0f59a8d0934/576eda4de4fcb5ab514ed5cd/58293236b3db2b0f3d3c3dbd/1518544651488/Fasika_08.JPG?format=2500w)

     * Notice the distinction between the style of the mural on the wall and everything else. We can try to somehow find a contrast to seperate the mural from the image. Probably need to research image segmentation and previous algorithms that have distinguished real photographs from paintings.

  * We need something that will work well to the detail, and speed of feed foward analysis will not matter as much as accuracy. But algorithms like YOLO might be neccesary, and I think I will eventually have to look into it.

2. Research on Semantic Segmentation (articles for now, research papers later):

  * [Semantic Segmentation with Deep Learning](https://towardsdatascience.com/semantic-segmentation-with-deep-learning-a-guide-and-code-e52fc8958823)
    * The author has an amazing github repository that is worth checking out: [github](https://github.com/GeorgeSeif/Semantic-Segmentation-Suite).
    * The basic backbone of basically most sementation neural networks is the U-Net Architecture:

    ![U-Net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png).

    * There are 3 parts to a U-Net:
      1. Contracting path
        * Comprised of 4 blocks, each block composed of:
          * 3x3 Convolution Layer + activation function (with batch normalization)
          * 3x3 Convolution Layer + activation function (with batch normalization)
          * 2x2 Max Pooling
        * at each pooling, feature maps double
      2. Bottleneck
        * between contracting and expanding paths
        * just 2 conv layers with batch norm. and dropout
      3. Expanding Path
        * 4 blocks, each block consists of:
          * Deconvolution layer with stride 2
          * Concatenation with the corresponding cropped feature map from the contracting path
          * 3x3 Convolution layer + activation function (with batch normalization)
          * 3x3 Convolution layer + activation function (with batch normalization)

    * Questions I have:
      * what does the expanding path even mean? This article wasn't very helpful because doesn't really describe what's happening or why certain traits are there, but just what's there.
      * Why do we need a bottle neck? Doesn't the contracting path alreadyt take care of squashing the image features together?
      * How exactly does the expanding path segment image??

    * Full-Resolution Residual Networks (FRRN)

  * [Image Segmentation: Kaggle experience (Part 1 of 2)](https://towardsdatascience.com/image-segmentation-kaggle-experience-9a41cb8924f0)
    * U-Net consists of encoder and decoder networks.
      * encoders are responsible for building a hierachy of features from simpler features (like edges and shapes to cars)
      * decoder is responsible for merging fine grained low level features with coarse high level features to restore the positional information  
    * very important to use pretrained models
      * model from [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) for encoder
      * model from [Automatic Instrument Segmentation in Robot-Assisted Surgery Using Deep Learning](https://arxiv.org/abs/1803.01207) for decoders

    * Questions
      * Aren't low level features supposed to be very unspecific (like lines and primitive shapes)? Or am I misinterpreting what fine grain is suppose to mean?
      * How exactly does a decoder merge features? Is it like a max pool?
      * How does a decoder tell you where the image is suppose to be (how does it keep the location)?
      * Does it really matter which pretrained model I use?

  * [What do we learn from region based object detectors (Faster R-CNN, R-FCN, FPN)?](https://medium.com/@jonathan_hui/what-do-we-learn-from-region-based-object-detectors-faster-r-cnn-r-fcn-fpn-7e354377a7c9)
    * most basic method for image segmentation is the sliding method: 
      * slide windows up, down, left, right. Classify each picture in the window.

    * Selective Search (SS)
      * find regions of interest (ROI)
      * start with each individual pixel as its own group
      * calculate the texture for each group, combine the two groups that are the closest
      * group smaller groups first to prevent one region from taking in everything

    ![Selective Search](https://cdn-images-1.medium.com/max/1600/1*ZQ03Ib84bYioFKoho5HnKg.png)

    * R-CNN
      * Uses creates 2000 ROI, which are fed into a CNN individually, and then passed through fully connected layers.

      ![R-CNN](https://cdn-images-1.medium.com/max/2600/1*Wmw21tBUez37bj-1ws7XEw.jpeg).

      * Flow chart:

      ![Flow Chart R-CNN](https://cdn-images-1.medium.com/max/2400/1*ciyhZpgEvxDm1YxZd1SJWg.png)

    * Fast R-CNN
      * instead of extracting features for each image patch from scratch, use a feature extractor to extract features from the start
      * then create ROIs  to combine with corresponding feature maps to form patches
      * use ROI pooling to change patches to a fixed size
      * feed the patches to a fully connected layer for classification and localization (where the image is located)

      ![Fast R-CNN](https://cdn-images-1.medium.com/max/2600/1*Dd3-sugNKInTIv12u8cWkw.jpeg) 

      * Flow Chart:
      ![FLow Fast R-CNN](https://cdn-images-1.medium.com/max/2600/1*fLMNHfe_QFxW569s4eR7Dg.jpeg)   

    * Faster R-CNN
      * same network flow, but different region proposal
      * ROIs come from the feature maps themselves

      ![New Region Proposal](https://cdn-images-1.medium.com/max/2600/1*0cxB2pAxQ0A7AhTl-YT2JQ.jpeg)  
    
      *  region proposal network (RPN) takes the output feature maps, uses 3 by 3 slide filter over the feature map. 
      * Objectiveness measures the box contains an object

      ![Region Proposal Network](https://cdn-images-1.medium.com/max/2600/1*z0OHn89t0bOIHwoIOwNDtg.jpeg)

    * Questions
      * I'm confused about the R-CNNs. Are they trained? I don't think so (the author of the article never explicitly said so), but then how is the R-CNN suppose to evaluate the results of running the R-CNN on the image? How does it measure objectiveness when there's no baseline?
      * How do you measure texture? What does texture even mean?
      * I understand that SVMs are great for finding boundaries between easily distinct classes (for example, in the Iris dataset, the classes are predefined: they're just the flowers). But what "classes" are the SVMs dividing? Is it just the box and not the box? But then if so, how does the SVM accurately know where to draw the boundary if the number of features (pixels) are so vast? Wouldn't the SVM perform badly because there's just so much input noise?   

  * [Fast R-CNN and Faster R-CNN](https://jhui.github.io/2017/03/15/Fast-R-CNN-and-Faster-R-CNN/)
    * Honestly, the pictures here are great. 
    * Turns out the R-CNNs are trained.

  * [Image segmentation with Mask R-CNN](https://medium.com/@jonathan_hui/image-segmentation-with-mask-r-cnn-ebe6d793272)

  ![Mask R-CNN](https://cdn-images-1.medium.com/max/2600/1*M_ZhHp8OXzWxEsfWu2e5EA.png)

  * [Design choices, lessons learned and trends for object detections?](https://medium.com/@jonathan_hui/design-choices-lessons-learned-and-trends-for-object-detections-4f48b59ec5ff)
    * Schemes and Loss Functions:
    * ![Models and Loss Functions](https://cdn-images-1.medium.com/max/2400/1*kWIv_EFsxqbTJoncadcY7A.png)
    * Feature Extractors:  
      * ResNet and Inception: acc more important than speed

    * Accuracy vs Time
      * ![Accuracy vs Time](https://cdn-images-1.medium.com/max/2600/1*7dJTcEv7vYAQyHbQ8QAZUA.png )

    * Faster R-CNN is more accurate while R-FCN and SSD are faster. 

  * [What do we learn from single shot object detectors (SSD, YOLOv3), FPN & Focal loss (RetinaNet)?](https://medium.com/@jonathan_hui/what-do-we-learn-from-single-shot-object-detectors-ssd-yolo-fpn-focal-loss-3888677c5f4d)
    * Might be interesting to check out, but I don't need it right now because single shots are less accurate, and we are looking for accuracy.

  * [Distinguishing paintings from photographs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.9304&rep=rep1&type=pdf)
    * Quite amazing that this was made in 2005.
    * Skimmed it, basically distinguishes paintings from photographs. Quite a long read.

  * [How to use DeepLab in TensorFlow for object segmentation using Deep Learning](https://medium.freecodecamp.org/how-to-use-deeplab-in-tensorflow-for-object-segmentation-using-deep-learning-a5777290ab6b)
    * Skimmed this article because using this requires preboxed objects, and our data will most likely not have preboxed objects. However, if we do decide to manually prebox objects, then this might be worth reading over.
    * Here's the [related paper](https://arxiv.org/abs/1706.05587).

  * [Semantic Segmentation with Deep Learning](https://towardsdatascience.com/semantic-segmentation-with-deep-learning-a-guide-and-code-e52fc8958823)
    * I don't really understand each model because the descriptions are very brief and dense. Also, there's no real value in remembering the model structures. But here are the models and some quick and useful info on them:
      * Full-Resolution Residual Networks (FRRN)
        * Slow but accurate
        * ![FRNN](https://cdn-images-1.medium.com/max/2400/1*LlYK2Pjemx3kNC61yVV-yA.png)
      * Pyramid Scene Parsing Network (PSPNet)
        * ![PSPNet](https://cdn-images-1.medium.com/max/2400/1*REgHs3PeemO3TIuyE46iRg.png)
      * The One Hundred Layers Tiramisu (FCDenseNet)
        * ![FCDenseNet](https://cdn-images-1.medium.com/max/2400/1*ioURm5w_miMj64DeLQ9H_g.png)
      * Rethinking Atrous Convolution (DeepLabV3)
        * can change the dilation rate to increase or decrease infomation
        * ![DeepLab](https://cdn-images-1.medium.com/max/2400/1*tn-mWYhEva2S6rEZg4oZGA.png)
      * Multi-Path Refinement Networks (RefineNet)
        * ![RefineNet](https://cdn-images-1.medium.com/max/2400/1*V6E6QIyB1BTOdbev4eDAqg.png)
      * There are also more in this article.

  * Methods For Segmenting Images
    * [Image Segmentation Algorithms Overview](https://arxiv.org/pdf/1707.02051.pdf)

**Thoughts**

That was alot to absorb, but I'll come back to it and reread my notes.

So how can we use image segmentation in our mural? 

The (slight) problem with the models that I read about is that a lot of the models require an image that is presegmented to train on. But what I want is to segment the image first, then extract the segmentation. Also, I want to train on a dataset that does not require segmentation because we only really want to look at style.

Our goal is to:
1. Train (usual convnet) from datasets. 
2. Use one of the texture algorithms to group parts of pictures. 
3. Draw a box around the group.
4. Run that image in the box through our convet.

Problems I can think of:
  * How do we ensure that the texture algorithms can pick up a mural? I'm worried that the segmentation algorithms will start boxing things inside the mural or even other objects, which is not what we want. We want to box only the mural. Is there a texture algorithm general enough that it is able to draw a box to distinguish the style of the mural of the picture in real life?
    * But at the same time, having boxes around items inside the mural can actually help us. It's quite possible that the machine learning algorithm will classify each smaller box with a different style, which can be interesting.
  * We need to crop the image so the image can be ran through the convet. Not sure if this is a big deal, but cropping decreases information. Though at the same time, people don't seem to worry too much about cropping images.
  * How do we deal with distortion?
    * For example, this image is completely flat, which is awesome.
    * ![ZEBRAA](https://static1.squarespace.com/static/58430e5a59cc68a03bb53543/58430f342994cab7bdab57f6/5b477b9f70a6ad5a7942e7e2/1531411620127/zebra_final_site.jpg?format=1500w)
    * But this image is slanted:
    * ![DEARRR](https://static1.squarespace.com/static/5898fb16579fb3651b5f836c/t/5a788771c830259c530cc210/1517852214088/paolo_pedini_berkley_mi_murals?format=750w)
    * This mural here is not in a rectangular shape.
    * ![BONEESS](https://rabbiteyemovement.at/rabbit/wp-content/uploads/2018/06/IMG_5213-1-820x1093.jpg)
    * Though I'm not entirely sure if it matters if the only thing we care about is the style.
  * There might not actually be a background (the entire photo is the mural). Is there a possible way to detect if there's no background?
    * I don't have an idea on how to answer this?

Some more resources to check out:

  * [Wikipedia Lol](https://en.wikipedia.org/wiki/Image_segmentation)
  * [Measuring visual quality of street space and its temporal variation: Methodology and its application in the Hutong area in Beijing](https://www.sciencedirect.com/science/article/pii/S0169204618310119).


## January 25, 2019

**Today's Progress**

### Write Up On Image Segmentation

1. What is image segmentation?

Image segmentation is essentially a method to divide the image into subimages, and analyze those subimages. Of course, this leads to the question, how exactly do we divide such image? I'll answer this later, but first, here's a visual below for what I mean. As we can see, we draw a box around each object that we wish to classify.

![Guy On A Horse](https://cdn-images-1.medium.com/max/1600/1*r9ELExnk1B1zHnRReDW9Ow.png)

2. How do we segment an image?
  * The brute force method is simply to use a sliding window, where we choose the size of the box, place the box on the image, and classify what's in the box. Then we slide the box up, left, right. For each slide, we repeat and try to classsify each image in the box. However, this is incredibly slow and inefficient.
  * A much better way to segment an image is to use Selective Search (SS) to find regions of interest (ROI). In selective search, we start with tiny intial regions, and we wish to grow those regions by locating two similar regions (in terms of mathemtically defined texture) and merging them together. We repeat this until no more regions are mergable. Then for each ROI, we place a box around it.

![Region Merging](https://cdn-images-1.medium.com/max/2400/1*_8BNWWwyod1LWUdzcAUr8w.png)

3. What are some neural network algorithms?
  * R-CNN
    * finds ROIs, and for each RIO, feed it through a CNN that is attached to fully connected layers that split into two labels (the class and the boundary box)
    * ![R-CNN](https://cdn-images-1.medium.com/max/2600/1*Wmw21tBUez37bj-1ws7XEw.jpeg)
  * Fast R-CNN
    * instead of extracting features for each patch, we extract the features from the initial image.
    * ![Fast R-CNN](https://cdn-images-1.medium.com/max/2600/1*Dd3-sugNKInTIv12u8cWkw.jpeg) 
  * Faster R-CNN
    * ROIs come from the feature maps themselves
    * ![New Region Proposal](https://cdn-images-1.medium.com/max/2600/1*0cxB2pAxQ0A7AhTl-YT2JQ.jpeg) 
  * There are many other variations of these algorithms, but knowing them isn't that important. But what we do need to keep in mind when picking an algorithm is the trade off between speed and accuracy. Some algorithms are incredibly fast, but lack accuracy. 

4. What are some resources that we can use for image segmentation?
  * For this, I mean libraries that have built in algorithms that support image segmentation (so we don't have to build one from scratch unless we really have to).
  * [Scikit Images](https://scikit-image.org/). Extension of Scikit-Learn.
    * Here's some links to get started:
    * [Label image regions](http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_label.html)
    * [Here's](https://www.scipy-lectures.org/packages/scikit-image/index.html) a more in-depth guide.
    * [Comparing edge-based and region-based segmentation](http://scikit-image.org/docs/dev/auto_examples/xx_applications/plot_coins_segmentation.html)
  * [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html)
    * [Image Segmentation with Watershed Algorithm](https://docs.opencv.org/3.4/d3/db4/tutorial_py_watershed.html)
  * Scikit Learn
    * [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#kd-tree)
    * [Spectral clustering for image segmentation](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html)


## January 30, 2019

1. Had three skype conversations, twice with Ben and once with both Ben and Professor Clark.
  * Basically discussed my findings on image segmentations and how we can use it. We also discussed more about artistic style for murals, and we feel that it may be too ambitious to try to classify the style of murals, mostly because of how undefined the mural styles are. It may also be tricky to train images on another style and apply it to the mural styles. The three of us decided that it would be a good idea to start smaller, so we switched to emotional classifications, which can be more transferable.
  * Also texted alot to Ben to discuss our findings and trajectories.

2. [Brief research](https://en.wikipedia.org/wiki/Art_and_emotion) on the relationship between art and emotion.
  * Biological (Evolutionary) Perspective
    * emotion is evoked from a person when the person absorbs meaning from the image stimuli and finds connection between the image and previous experiences.
    * humans tend to search for patterns and symmetry
    * brightness and open landscapes connect to calmness and happiness
    * darkness and obscureness connects to anxiety and fear
  * Types of Emotions That Images Evoke
    * still an open debate
    * anger, confusion, happiness: basic
    * emotions are subjective
    * Liking Emotions
      * does pleasure and displeasure towards the artwork count as emotions?
      * researchers found that how well a person enjoyed a painting was correlated to how well they understood the painting and connected to it
      * emotional feeling of beauty or aesthetic experience: is this actually an emotion?
    * Knowledge Emotions
      * reactions from thinking and feeling 
      * interest
        * positive perception of what is new, complex, and unfamiliar
      * confusion
        * opposite of interest
        * stems from uncertainty
      * surprise
        * new and unexpected
        * expectations were not met
    * Hostile Emotions
      * anger
      * fustration
      * aggression
      * disgust
      * contempt
    * Self-conscious emotions
      * from reflection of oneself
      * pride
      * guilt
      * shame
      * regret
      * embarassment

  * Great and comprensive connection between art and emotion. [Here](https://www.iep.utm.edu/art-emot/)

3. Started looking through more papers on emotional analysis.
  * finding papers on the intersection between artworks, machine learning, and emotions turns out to be pretty difficult. Took some time, but here are some papers that I found that were useful and (hopefully) applicable:

  * [EMOTIONAL VALENCE CATEGORIZATION USING HOLISTIC IMAGE FEATURES](https://www.researchgate.net/publication/221122984_Emotional_valence_categorization_using_holistic_image_features)
    * Published in 2008
    * training data comes from International Affective Picture System (IAPS), the standard emotion invoking dataset
      * about 700 photographs, cateogorized by emotional valence (from negative to positive)
      * of the 700, 400 are classificed to anger, awe, disgust,fear, sadness, excitement, contentment, and amusement
      * 60 participants labeled on a scale from 1 to 7 each emotion above.
    * used Support Vector Machine on extracted features from images
      * They used Wiccest features and Gabor filters.
    * results weren't that great. Accuracy for each class ranged from 50% to 60% (50% being the baseline.)
  
  * [Affective Image Classification using Features Inspired by Psychology and Art Theory](http://delivery.acm.org/10.1145/1880000/1873965/p83-machajdik.pdf?ip=128.135.98.24&id=1873965&acc=ACTIVE%20SERVICE&key=06A6A3A8AFB87403%2E37E789C11FBE2C91%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1548904715_5aee417e5c7168e4e17b8f6bb4bcc9be)
    * Emotional Semantic Image Retrieval (ESIR): analysis and retrieval of images at the affective level (emotional and subjective based)
    * uses both psychological and art theories
    * modeling emotions:
      * dimensional approach: represent emotions as coordinates in a vector space
      * category approach: assign descriptive words to regions of the space
      * this paper used category approach
    * Examples:
      * [K-DIME](http://discovery.ucl.ac.uk/3367/1/3367.pdf): uses neural networks 
      * Colombo et al.: defined features for hue, saturation, warmth and luminance contrast, and color harmony between distinct image regions
    * Dataset that they [used](http://www.imageemotion.org/).
    * did feature extraction, then ran the features through the machine learning models (like SVM, Random Forests)
      * Some features include:
        * color
          * Saturation and Brightness
          * Hue (shade)
          * Colorfulness (measured by EMD)
          * Color Names
          * Itten contrasts (combinations of color for emotional effects)
        * texture
          * Wavelet-based features (measures spatial smoothness in images)
          * Tamura texture features (coarseness, contrast and directionality)
          * Gray-Level Co-occurrence Matrix (contrast, correlation, energy, and homogeneity of an image)
        * Composition 
          * Level of Detail (how detailed was the images)
          * Low Depth of Field (blurring of the background)
          * Dynamics (lines that induce emotions)
          * Rule of Thirds (main object should be located in the middle)
        * Content
          * human faces
          * skin
        * the author did not explain the complicated algorithms used to measure these features
    * Output Labels:
      * Positive: Amusement, Awe, Contentment, Excitement
      * Negative: Anger, Disgust, Fear, Sad
    * Datasets
      * IAPS
      * set of 807 artistic photographs
      * set of 228 peer rated abstract paintings
      * combined all 3
  
  * Checked out the [website](http://www.imageemotion.org/) for the above paper
    * Powerpoint Presentation on the Website.
      * Skimmed this.
      * really good for looking at the images
    * Getting the data
      * For [IAPS dataset](https://csea.phhp.ufl.edu/media.html). Pretty annoying that I have to ask a professor to sign a waiver for this data.
      * but the site does contain data from the other two datasets it used

  * [Exploring Principles-of-Art Features For Image Emotion Recognition](http://delivery.acm.org/10.1145/2660000/2654930/p47-zhao.pdf?ip=128.135.98.24&id=2654930&acc=ACTIVE%20SERVICE&key=06A6A3A8AFB87403%2E37E789C11FBE2C91%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1548904637_ee7f6bf55b2830bf62c3f9c306654a0b)
    * published in 2014
    * argues that there are many problems with using low level features 
      * low level features include color, texture, line, shape
      * these low level features need to be carefully arranged to have a link towards emotions
      * are not invariant to different arrangements
      * not interprebable by human beings
    * extract  Principles-of-art-based emotion features (PAEF) for classification
      * balance, emphasis, harmony, variety, gradation, movement, rhythm, and proportion
      * combinations of these evoke different emotions
    * also uses (IAPS) and the same dataset as the above article
    * also uses categorical emotion states
    * PAEF features:
      * balance (feeling of equilibrium and symmetry)
      * emphasis (aka contrast) (stressing of differences of certain elements)
        * uses Itten's color contrast and Sun's RFA (rate of focused attention on the image)
      * harmony (aka unity) (way of combining low level features)
        * computed harmony intensity for each pixel
      * variety (create complicated image by combining different elements)
      * gradation (way of combining images through a series of gradual changes)
      * movement
      * the author included complicated equations for measuring each feature
    * achieved better results than the previous articles

  * [Context effects on emotional and aesthetic evaluations of artworks and IAPS pictures](https://www.sciencedirect.com/science/article/pii/S0001691814001541)
    * Incredibly long paper without pictures
    * published in 2014
    * more of a qualatitive analysis on the paper above

  * [Aesthetics and Emotions in Images](https://ieeexplore.ieee.org/abstract/document/5999579)
    * published in 2011
    * qualitative description of inferencing emotions from artworks
    * possibly worth reading, but very long

  * [Recognizing Emotions from Abstract Paintings using Non-Linear Matrix Completion](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Alameda-Pineda_Recognizing_Emotions_From_CVPR_2016_paper.pdf)
    * apparently matrix completion has been great for mulit-label image classification and were mostly a linear classification model, though I have no idea what matrix completion is.
    * contains a bunch of matrix multiplication and equation manipulations
    * performed better than the previous models
    * contains links to great datasets to check out
    * maybe its because I don't understand the math but how does matrix completion classify images? Is it combined with another model?
    * Research from [Wikipedia](https://en.wikipedia.org/wiki/Matrix_completion) on matrix completion
      * matrix completion refers to filling in missing entries in a matrix
      * useful for filling in missing pixels in computer vision

  * [Multi-level region-based Convolutional Neural Network for image emotion classification](https://www.sciencedirect.com/science/article/pii/S0925231218315145)
    * published in 2018
    * used FPN variation of the CNN to classify local emotions in the image as opposed to the traditional methods of classifying the entire image at once
    * uses a multi-level r-cnn to extract local representations of images
    * Pipeline:
      * ![FPN Pipeline](https://ars.els-cdn.com/content/image/1-s2.0-S0925231218315145-gr2.jpg).
      * used FPN to extract the deep features maps, which would combine high level semantic features with low level deep features
      * ResNet101 as backbone
      * ![Backbone](https://ars.els-cdn.com/content/image/1-s2.0-S0925231218315145-gr3.jpg)
    * used emotion class probability output rather than hard class label since emotions are subjective
      * also because humans would also probably feel a distribution of emotions rather than one
    * used categorical emotion states (CES)
    * one difference from the way the authors used r-cnn is that they want to find regions of interests that contain emotions and not based on just content
      * this is a lot more challenging not only because emotions are subjective, but both objects and surrounding background contribute to the emotions
      * to do this, the pipeline has been modified to find the probability of a region evoking emotion
    * Mikels’ Wheel: used to determine the similarity between two emotions
    * dataset is a lot more comphrensive than the previous papers
      * 23,308 labeled from flicker and instagram
      * 2000 from EmotionRol
      * IAPSsubset
      * ArtPhoto : 800
      * 228 Abstract paintings
    * loss function was not softmax (like the other papers) since the results are probability distributions.
      * rather, they used Lp distances.
    * results: better than all previous works
    * this is a great paper to reread and for tracing its citations

  * [Fine-tuning Convolutional Neural Networks for fine art classification](https://www.sciencedirect.com/science/article/pii/S0957417418304421)
    * classifies artist, genre, style, time period, association with national artistic context
    * dataset used: 
      * wikiart: 133000 artworks
      * Genres in the dataset:
      * ![Genres Wikiart](https://ars.els-cdn.com/content/image/1-s2.0-S0957417418304421-gr1.jpg)
      * Web Gallery of Art (WGA): labeled with genre, art historical period, school and timeframe (in 50 years steps) in which the artists were active
    * contains specifics on how the model was set up and tricks they used to improve accuracy
      * honestly nothing new or noteworthy
    * contains a bunch of charts comparing the models

## January 31, 2019

1. Phone call with Alexis.
  * Talked about possible ways we can use the synonym that I generated. We thought it would be useful to run all the generated words through Yelp and see which synonym pops up the most. Need confirmation from Hyesun before I do this.
  * Talked about ways we can do more mural analysis.
    1. emotional response analysis (this can be pretty simple like gloomy, sad, happy, calm)
    2. classifying murals vs graphitti 
    3. content analysis (what exactly is in these murals: people, animals, whatnot)
    4. image of text to text (since Alexis said some murals have text in them, like "Freedom" or "Liberty", etc. It would be incredibly helpful for finding out what kind of atmosphere or vibe these text invoke. Also, it would also be great to be able to find what language the text contains (text in Spanish vs text in English, etc) 
  * Talked about the role of music in cafes.
    * hard to do because we would need to ask the cafes for their playlists. Not sure how to go from here.

## February 6, 2019

1. Talk with Ben. My goals:
  * talk to Clark about the different analysis that we are going to do (emotional, content, mural vs graphitti)
  * read more in depth on the paper (understand every detail)
  * look more into the psychological aspects of emotions

2. We need to be able to use this classifier to tie whatever attributes to geographical locations.

  * Mural maps in [LA](https://www.muralmapla.com/).

## February 7, 2019

1. Email to Professor Clark for clarification. 

    >> Dear Professor Clark,

    >> I just want to recap on what I and Ben have done on the art project and how we can connect it with Scenes variables.

    >> So we are currently trying to build a model that can detect the emotions from a mural. 
    I've personally read a lot of literature combining machine learning and art. 

    >> I've searched on Google Scholar with key terms:
    >> "convolutional neural network" and art and emotion. The results produced about a dozen papers that were worth reading, and I read most of them (took notes on the log).

    >> But searching on Google Scholar:
    >> "convolutional neural network" and mural produced no meaningful result, indicating that what we needed to do was build a model that works for general art, and apply it to murals.

    >> After reading many papers on the possible techniques, we decided on one that we want to replicate because it was the newest one and it was built to fix the problems of all the other papers. It is also built on top of huge amounts of psychological literature involving art and emotions. I've also read a lot of papers on the psychology of emotions and how they relate to art (took notes on my log). The emotions that the model can rate are:
      * anger
      * awe
      * disgust
      * fear
      * sadness 
      * excitement
      * contentment
      * amusement

    >> Ben sent an email to the authors of the paper asking for their code and dataset. If they provide it to us, it would save a lot of time, and we can apply the code onto murals. If not, we will have to replicate the paper ourselves.

    >> So how we can connect it to scenes variables? Pulling from the meeting on Wednesday, we believe that we can use the model to rate emotional responses from murals in different geographical locations. Once we have these ratings, we can use geographically weighted regression to correlate these emotions with scenes variables and political connotations.

    >> It would be interesting to use this to see the Bohemian cleavages in different areas. 
    Tying this to the Yelp data, we can look at keywords in Yelp reviews that somehow connect to these emotions.

    >> My theories for each emotion:
    >> anger, fear, sadness: If a mural has a rating of high anger, fear, or sadness, we have to ask why. Is there a political movement of activism surrounding the mural? Are people dissatisfied with something? This leads to a natural possible test of correlation between anger and variables like income, quality of life (measured by amenities), feeling of injustice (connection to the scene's book of egalitarianism). On the opposite end, the emotion of contentment can also be linked to the same variables.

    >> awe: If a mural has a high rating of awe, it may be possible that the murals may be trying to attract visitors and tourists. This directly tied to amenities since places that try to increase tourism would likely to also have a lot of amenities. We would also expect that the location of the mural to be in a Bohemian environment.

    >> disgust: I doubt there would be any high ratings of disgust in murals, but we may be surprised. 

    >> excitement: More ties to Bohemian culture and self-expressionism.

    >> These connections with scenes variables are preliminary. I've been talking to Andrew, who I feel can provide extremely valuable insight into more of these connections.

    >> Last thing to address: why machine learning and not any other method? 
    Machine learning is the only realistic way to analyze art in a quantitative fashion. Doing a search on google scholar will show that the top results will be applying machine learning to analyze art.
    And why quantitative over qualitative?
    Because quantitative approaches are extremely scalable. If we build this and it works for a city, this model will be an incredible tool to use when trying to analyze murals globally. Furthermore, we feel that qualitative analyze is too fickle, inconsistent, and time-consuming.

    >> I'll send another email later detailing how we can use Yelp data to connect with scenes variables.

    >> Best,
    >> Jin Li

2. Got approved for RCC. World just opened up. Also, Ben got access to GPUs in TTIC Uchicago, so that's great.

## February 8, 2019

1. Tracking down the dataset.
  * http://www.imageemotion.org/.
    * need to request access to (IAPS) dataset. Here's the [site](http://csea.phhp.ufl.edu/media.html) to access it.
    * but has others including 807 artistic photographs, 228 peer rated abstract paintings.
  * The original [paper](https://arxiv.org/abs/1605.02677) that created 23000 images from Amazon Turk. Tried to google for the dataset, but couldn't find it. I was thinking to email the authors for the dataset.
    * Here's one of the [guys](http://www.cs.rochester.edu/u/qyou/).
  * EmotionalROI Database [here](http://chenlab.ece.cornell.edu/downloads.html).

## February 9, 2019

1. Talked with Ben. After emails, we both thought it was best to scratch the idea of trying to analyze murals because we started to realize that no one was actually working on murals. We also talked with Christina about our ideas, and there were problems with emotional classification because its hard to generalize emotions from a dataset to what we are looking at because different people have different reactions to the same mural.

2. In a sense, we may have to restart our idea proposal. However, it does not neccesarily mean we are at square one; a lot of what I learned about image segmentation and deep learning modeling can still be applied. The only difference is that how we are applying it would be different.
  * Our idea was to try to ground image analysis on architecture, because Hyesun did her PhD on it, and it would have the highest likelihood of being approved. We also think that there's no way that machine learning and artificial intelligence can not be relevant to the field of sociology. There's just so much data avaliable that we are not using, and sociology is about the study of people and how they interact and why. And what better way to study this than large scaled machine learning?
  * My current goal is to search for possible datasets of architecture that we can use, and Ben's goal is to look through the literature first instead of the model first. Taking Clark's criticism, we feel that it may be our first priority to look at the causal links before we look at how to test these links.

3. [Measuring the Unmeasurable: Urban Design Qualities Related to Walkability](http://www.ia.arch.ethz.ch/wp-content/uploads/2011/10/HS11L2_Ewing_Handy-2009.pdf?fbclid=IwAR0wHOEf5aMJZJmALV3fW-daXxJqk4MlcGhORN1leGKeII5z6NC6GBcweEA)
  * published in 2009
  * tries to quantatively measure subjective qualities of urban streets
  * The 5 urban qualities that it tried to measure:
    * imageability
      * quality of a physical environment that evokes a strong image in an observer. Landmarks, distinctive buildings.
      * related to the sense of place, legibility, enclosure, human scale, transparency, linkage, complexity and coherence
    * enclosure
      * lines of sight are blocked
      * visual termination points
    * human scale
      * height, width of buildings
    * transparency
      * glass windows
    * complexity
      * number of noticable differences to the viewer
  * perception: process of being aware of sensory infomation
  * physical features, urban design qualities, individual reactions: can influence the way an individual feel the environment
  * Thoughts:
    * Are these measurements machine learnable? Is there a dataset that contains these measurements?

4. [A machine learning method for the large-scale evaluation of urban visual environment](https://arxiv.org/pdf/1608.03396.pdf?fbclid=IwAR1sDYgSqeqZPMu9WREUPIiZnRt9xIW_84SMjyztYmCtHWG9jS0_qOzdhOg).
  * Skimmed this paper
  * use computer vision to evaluate the urban visual environment
  * Quality of facade determined by:
    * Composition
    * Material
    * Detail
    * Color
    * Maintenance
  * used Beijing as the case of study
  * manually labeled building and street images
    * their data is [here](http://www.urbanvisionstudy.com/). But link doesn't seem to be working.
  * limitations of their paper:
    * size of expert label is small
    * CNN has trouble capturing details

5. [Using Convolutional Networks and Satellite Imagery to Identify Patterns in Urban Environments at a Large Scale](https://arxiv.org/pdf/1704.02965.pdf?fbclid=IwAR2SWAjXztZ100FlZkakmOhnskqVlXtjzsVOcZZ03hAtQ3HoPZOSKgWBkrA)
  * Skimmed
  * classified urban environments
    * Agricultural + Seminatural areas + Wetlands
    * Airports
    * Forests 
    * Green urban areas 
    * High Density Urban
    * Fabric
    * Industrial, commercial, public, military
    * Low Density Urban
    * Fabric
    * Medium Density Urban Fabric
    * Sports and leisure facilities
    * Water bodies

6. Possible Datasets:
  * Searched on Google: google street view dataset
    * [Google Street View Pittsburgh Research](http://classif.ai/dataset/google-street-view-pittsburgh-research/)
    * [25 million images Dataset](https://github.com/amir32002/3D_Street_View)
      * unlabeled
    * [Using deep learning and Google Street View to estimate the demographic makeup of neighborhoods across the United States](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5740675/)
      * skimmed
      * income, race, education, and voting patterns can be inferred from cars
  * Searched on Google: geographical image dataset
    * [Free GIS Data](https://freegisdata.rtwilson.com/)