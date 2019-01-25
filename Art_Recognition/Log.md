# Log Version 21

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
      * ![Accuracy vs Time](https://cdn-images-1.medium.com/max/2600/1*7dJTcEv7vYAQyHbQ8QAZUA.png)
