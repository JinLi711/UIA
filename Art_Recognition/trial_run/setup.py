"""
This is a script for setting up all clustering models, 
as all the models will have similar set ups.

It includes:
    default variable assignment
    brief visualizations
    image files preprocessing
"""


import os

import matplotlib.pyplot as plt
import numpy as np

# image processing
from PIL import Image
import skimage.io
import skimage.transform


#======================================================================
# Default Variable Assignments
#======================================================================


train_path = "art_images/dataset_updated/training_set"
test_path = "art_images/dataset_updated/validation_set"
corrupt_path = "art_images/dataset_updated/training_set_corrupted"

categories = ['drawings', 'engraving', 'iconography', 'painting', 'sculpture']

category_embeddings = {
    'drawings': 0,
    'engraving': 1,
    'iconography': 2,
    'painting': 3,
    'sculpture': 4
}

width = 96 # 368
height = 96 # 352
n_channels = 3


#======================================================================
# Brief Visualizations
#======================================================================


def view_freq(categories, training_dataset_path):
    """
    Create a bar graph for visualizing categorical frequencies

    :param categories: list of categories
    :type  categories: list
    :param training_dataset_path: relative path of the training dataset
    :type  training_dataset_path: str
    """

    n_imgs = []
    for cat in categories:
        files = os.listdir(os.path.join(training_dataset_path, cat))
        n_imgs += [len(files)]

    plt.bar([_ for _ in range(len(categories))], n_imgs, tick_label=categories)
    plt.title("Category Frequencies")
    plt.show()


def view_images(categories, training_dataset_path):
    """
    View one image from each category

    :param categories: list of categories
    :type  categories: list
    :param training_dataset_path: relative path of the training dataset
    :type  training_dataset_path: str
    """
    
    n_categories = len (categories)
    fig, axes = plt.subplots(nrows=1, ncols=n_categories, figsize=(15, 3))

    cat_cpt=0
    for cat in categories:
        category_path = os.path.join(training_dataset_path, cat)
        img_name = os.listdir(category_path)[1]
        img = skimage.io.imread(os.path.join(category_path, img_name))
        img = skimage.transform.resize(img, (width, height, n_channels), mode='reflect')
        axes[cat_cpt].imshow(img, resample=True)
        axes[cat_cpt].set_title(cat, fontsize=8)
        cat_cpt += 1

    plt.show()


#======================================================================
# File Preprocessing
#======================================================================


def get_file_names(categories, training_dataset_path, test_dataset_path):
    """
    Get all the file names and its category

    :param categories: list of categories
    :type  categories: list
    :param training_dataset_path: relative path of the training dataset
    :type  training_dataset_path: str
    :param test_dataset_path: relative path of the test dataset
    :type  test_dataset_path: str
    :returns: (list of tuples of train, where first element of tuple is file name,
               and second element is the category, list of tuples of test)
    :rtype:   (list, list)
    """

    training_data = []
    for cat in categories:
        files = os.listdir(os.path.join(training_dataset_path, cat))
        for file in files:
            training_data.append((os.path.join(cat, file), cat))

    test_data = []
    for cat in categories:
        files = os.listdir(os.path.join(test_dataset_path, cat))
        for file in files:
            test_data.append((os.path.join(cat, file), cat))
    return training_data, test_data


def move_bad_file(tuples_list, dataset_path, corrupt_path):
    """
    Move corrupted images to new folder.

    :param tuples_list: list of tuples, 
                        where first element of tuple is file name,
                        and second element is the category,
    :type  tuples_list: list
    :param dataset_path: relative path of the dataset
    :type  dataset_path: str
    :param corrupt_path: relative path where corrupted files are moved
    :type  corrupt_path: str
    """

    indexes = np.arange(len(tuples_list))
    n_samples = len(indexes)
    for i in range(n_samples):
        t = tuples_list[indexes[i]]
        path_name = os.path.join(dataset_path, t[0])
        try:
            img = Image.open(path_name)
        except FileNotFoundError:
            # corrupt file has already been moved 
            pass
        except (IOError, SyntaxError) as e:
            print("Bad file:", t[0])
            # move file
            os.rename(path_name, os.path.join(corrupt_path, t[0]))
