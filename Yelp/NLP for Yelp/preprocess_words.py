"""
This module is to:

    Preprocess words.
    Lemmatize the words. 
    Remove stems.
    Count frequencies.
"""

import glob

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
import nltk
from collections import Counter


def getReviews (files, processed_path, strip):
    """
    Extract reviews from raw data.
    
    :param files: File path
    :type  files: str
    :param processed_path: File path for the extracted reviews
    :type  processed_path: str
    :param processed_path: Folder name to strip
    :type  processed_path: str
    :returns (list of dataframes, list of business names, list of csv file names)
    :rtype (list, list, list)
    """
    
    csv_files = glob.glob(files)
    names = [name.strip(strip).strip('.csv') for name in csv_files]
    csv_reviews = []
    review_files = pd.DataFrame ()
    for (i, file) in enumerate (csv_files):
        csv = pd.read_csv (file)["review-content"]
        csv = csv.dropna().reset_index().drop('index', axis=1)
        csv.columns = [names[i]]
        csv_reviews.append (csv)
        review_files = pd.concat ([review_files, csv], axis=1)
        
    review_files.to_csv (processed_path)
    return (csv_reviews, names, csv_files)


def createWordList (reviews, names, remove_punct=True):
    """
    Create a list of reviews.
    
    :param reviews: List of dataframes
    :type  reviews: list
    :param names: List of business names
    :type  names: list
    :param remove_punct: If true, remove punctuations.
    :type  remove_punct: bool
    :returns: A list where each element is string of all reviews for one business. 
    :rtype:  list
    """
    
    word_list = []
    for (i, csv) in enumerate (reviews):
        all_words = ""
        for (index, row) in csv.iterrows():
            all_words += row [names[i]]
        all_words = all_words.lower()
        
        if remove_punct:
            word_list.append (re.sub('[()!@%^&*-+\$.,?"#\xa0]', ' ', all_words))
        else:
            word_list.append(all_words)
    return word_list


def findWordFreq (word_list, names, threshold = 20, directory=None):
    """
    Count the word frequency in each element of the list.
    Filter out the common words that do not provide any valuable information.
    Keep keywords.
    
    :param word_list: A list where each element is string of all reviews for one business. 
    :type  word_list: list
    :param names:
    :type  names:
    :param threshold: Minimum number of word appearances
    :type  threshold: int
    :param directory: Directory of keywords file
    :type  directory: str
    :returns: A dictionary of dictionaries. 
              Each key is a business name, and each value is a dictionary.
              In that dictionary, the keys are words and frequencies are the values.
    :rtype:   dict
    """
    
    common_words = pd.read_csv ('Word_Lists/commonwords.csv')['WORDS'].values.tolist()
    keywords = pd.read_csv (directory)['WORDS'].values.tolist()
    csv_counter = {}
    for i in range (len (word_list)):
        unique_words = Counter (word_list[i].split())
        filter_unique_words = {}
        for key in unique_words:
            # if (not (key in common_words)) and ((key in keywords) or (unique_words[key] > threshold)):
            #     filter_unique_words[key] = unique_words[key] 
            if (key in keywords):
                filter_unique_words[key] = unique_words[key] 
        csv_counter[names[i]] = filter_unique_words
    return csv_counter


def createplot (csv_counter, threshold=0):
    """
    Creates plots for each business based on word frequencies.
    Saves plots to folder "Plots".
    
    :param csv_counter: A dictionary of dictionaries. 
              Each key is a business name, and each value is a dictionary.
              In that dictionary, the keys are words and frequencies are the values.
    :type  csv_counter: dict
    :param threshold: cut off of frequency for word count.
                      If cutoff is not met, do not include the word in the plot.
    :type  threshold: int
    """
    # Create the bar graphs of top words for each business
    # Output the bar graphs to the folder "plots"
    df_occurences = pd.DataFrame (csv_counter)
    for column in df_occurences:
        name = column#.strip('scraped/').strip('.csv')
        plot = df_occurences[column].dropna()
        plot = plot[df_occurences[column] > threshold]
        plot.plot(kind="bar")
        plt.title(name)
        fig = plt.gcf()
        fig.set_size_inches(15,8)
        plt.savefig('Plots/' + name + '.png', bbox_inches='tight')
        plt.show()


def pipeline ():
    """
    Put everything together.
    """
    csv_reviews, names, csv_files = getReviews ("Raw_Scraped_Data/*.csv", 
                                            'Processed_Data/all_reviews.csv')
    word_list = createWordList (csv_reviews)
    csv_counter = findWordFreq (word_list)
    createplot(csv_counter)

def GroupByLocation (names, word_list):
    """
    :param names: list of names of businesses
    :type  names: list
    :param word_list: A list where each element is string of all reviews for one business. 
    :type  word_list: list
    :returns: (list of group names, list of strings of concated reviews)
    :rtype:   (list, list)
    """
    
    listOfGroups = []
    for name in names:
        listOfGroups.append ( name.split('_')[0])
    setOfGroups = set (listOfGroups)
    
    placeAndReviews = {}
    for group in setOfGroups:
        placeAndReviews[group] = ''
        
    for i in range (len (names)):
        group = names[i].split('_')[0]
        review = placeAndReviews.get(group)
        placeAndReviews[group] = review + word_list[i]
     
    groups = []
    reviews = []
    for key, val in placeAndReviews.items():
        groups.append (key)
        reviews.append (val)
    #return placeAndReviews
    return (groups, reviews)


def groups_to_json (names, reviews, file_name):
    """
    Given keys and values, dump out a json file.
    
    :param names: List of groups
    :type  names: list
    :param reviews: List of strings, where each string are all the reviews for one group
    :type  reviews: list
    :param file_name: File name of output json
    :type  file_name: str
    """
    import json
    dict_of_reviews = {}
    for i in range (len (names)):
        dict_of_reviews[names[i]] = reviews[i]
        
    with open(file_name, 'w') as outfile:
        json.dump (dict_of_reviews, outfile)
    #return dict_of_reviews