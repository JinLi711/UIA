# Medium Classification

## Objective

Train a neural network to classify the medium of a piece of art.

## What is a medium?

In art, the medium is the material used to create an artwork. For example, in the [BAM dataset](https://bam-dataset.org/#explore) (which is what I plan to use to train), the mediums are:

  * 3D Graphics
  * Comic
  * Pencil Sketch
  * Oil Paint
  * Pen Ink
  * Vector Art
  * Water Color

One could argue that medium can be used as a way to distinguish style. However, after seperating the arts based on mediums, we plan to run the art through another neural network that determines the style.

## BAM Dataset

Currently, I'm using the smaller BAM dataset, which contains metadata for 390,000 images. Note that this is metadata, and does not actually contain the images themselves. The dataset, though, does contain links to the image, which are downloadable.

### Metadata

As far as what is valuable for us, the data that we are going to focus on are the labels (the ids), the links to the image, and the crowd labeled scores of the images.

  * ids (called mid in the dataset)
  * project id. Modules within the same project are related in style.
  * Links
    * The links all start with: "https://mir-s3-cdn-cf.behance.net/project_modules/disp/" if it works.
    * If the link doesn't work (meaning there is no image available), then the link seems to start with: "https://mir-cdn.behance.net/v1/rendition/project_modules/disp/"
    * [Link example](https://mir-s3-cdn-cf.behance.net/project_modules/disp/a9e0f21065.55f7265cdb7b3.jpg) 
  * Scores
    * Higher score indicates higher confidence
    * Scores are negative
    * Scores are assigned to each category. 
    * Category examples:
        * content_bicycle
        * content_bird
        * content_building
        * content_cars
        * content_cat
        * content_dog
        * content_flower
        * content_people
        * content_tree
        * emotion_gloomy
        * emotion_happy
        * emotion_peaceful
        * emotion_scary
        * media_3d_graphics
        * media_comic
        * media_graphite
        * media_oilpaint
        * media_pen_ink
        * media_vectorart
        * media_watercolor

## Plan 

This is the current plan after initial exploration. This is bound to change.

### Step 1: Get data

1. Open SQLlite in python. 
2. Select only the id, link, and scores for each image. 
3. Remember to dump everything else to reduce memory usage.
4. Open the sql data into a python dataframe.
  * for the scores, pick the highest scores and the corresponding label for each output class
5. Do neccesary data type conversions (like what I did in my water pump project) to further reduce the memory use.
6. Scrape websites using link.
7. Resize
8. Download images.
  * I need a way to track where I'm at so I don't have to redownload everything everytime I run the python script. I think a good way to do this is to create an external file that contains where I stopped.
  * I also have to keep track of missing images. If we try to retrieve an image that is dead, there's an http 404 error. How will I store this result?
  * The image name will be the corresponding ID.
  * Downloaded paths

### Step 2: Visualization

1. Download a small set of the images for visualization. The images should represent all classes.
2. Plot the images against their labels.

### Step 3: Preprocess

1. Since we are only focusing on the style and mood, we can remove the content columns
2. For style, select the category with the highest confidence score. We can create one new column for style and another new column for mood. The column will contain elements that indicate the most likely category.
3. Combine the dataframes (the one for scores and the one for based on ID (I think the columns should already be aligned in the dataset.)
4. Split into train, validation, and test set. Remember to use stratified random sampling, since the categories are unevenly distributed. In addition, neural networks perform worse if batch sizes do not have diversity (we don't want a batch that contains only water color labels).
5. Convert categories into numerics. Remember to remember what category each number is assigned to.
6. Resize the image to a standard size. 128 * 128 is usually a good option. In addition, scale the images by dividing by 255.

### Step 4: Model Building

1. Remember to set up check points so if the model stops, I can resume training.
2. Send an url request to the image source, and upload it into python as a numpy array. There's no need to download it, since we only care about the numeric representation.
3. Build a CNN. Need max pooling, seperable Conv 2D, batch normalization, dropout. Should map to TWO dense layers (one for style, another for mood).
4. Do image augmentation. (flipping, rotating, zooming.) Need to think more about how to augment, and what agumentations make sense. For example, changing the color is not a good idea because color heavily influences mood.

### Step 5: Model Evaluation

1. Plot accuracy and validation loss.
2. Repeat the training with different hyperparameters. Or we can also use python libraries that help find optimized hyperparameters.
3. Build a machine learning model on top of the CNN for black box evaluation (like what I did in the water pump project).
4. Evaluate on an entirely different dataset to check if the data we are using is a good transfer to other artworks. It should be fine because the authors of the BAM dataset found that the model transfered pretty well, but it is smart to check anyways.

### Step 6: Model Deployment

1. Professor Clark was talking about this website that geocodes artworks and locations. Ben and I thought that it would be a good idea to scrape that website, run our CNN through those images, and say something about the distributions of artworks in different neighborhoods.


### Things To Keep In Mind

  * check the numeric representation of images (different libraries interpret the channels differently)


## References

For information on loading the data, check [here](https://gist.github.com/gcr/c0e13bd205ed593f022ae0ad863e4ee2).