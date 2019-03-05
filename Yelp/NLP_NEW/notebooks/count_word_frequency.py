"""
Count the frequencies of words in Yelp reviews.
"""


import spacy
import unidecode
import re
from collections import Counter
from collections import defaultdict
import pandas as pd
import json

import generate_synonyms as gs


nlp = spacy.load('en_core_web_sm')


def normalize_text(text):
    """
    Normalize the text by:
            lowercasing
            removing diacritics
            replacing certain characters
            removing duplicate spaces and delimiters
            lematizing words

    :param text: string
    :type  text: str
    """

    # this is missing characters: ',.?!|/
    rm_char = r'[~`#$%^&*()_+=\[\]{}\\;:<>@-]|\d'
    text = re.sub(rm_char, ' ', text)

    # removes duplicate spaces
    text = ' '.join(text.split())

    text = text.lower()
    text = unidecode.unidecode(text)

    # convert to spacy text
    spacy_text = nlp(text)
    # -PRON- refers to pronouns
    norm_text = " ".join([token.lemma_ for token in spacy_text])
    return norm_text

    

class KeyWords:
    """
    Keywords to search in Yelp reviews.
    """

    def __init__(self, word_list):
        """
        :param word_list: list of the keywords to search
        :type  word_list: list
        :param word_set: set of normalized words
        :type  word_set: set
        :param synsets: set of synsets for the words
        :type  synsets: set
        """
        self.word_list = word_list
        self.word_set = {}
        self.synsets = {}

    def normalize_words(self):
        """
        Normalize each keyword.
        Insert the results in word_set.
        """

        word_list = list(set(self.word_list))
        norm_word_set = set([normalize_text(word) for word in word_list])
        self.word_set = norm_word_set

    def include_synonyms(
        self, 
        file_dir="../word_lists/synonyms/", 
        filter_words_file="filter_words.json", 
        filter_synsets_file="filter_synsets.json"):
        """

        """

        with open(file_dir + filter_words_file) as json_file:  
            word_filter = json.load(json_file)
    
        with open(file_dir + filter_synsets_file) as json_file:  
            synset_filter = json.load(json_file)

        pos_synsets = gs.divide_words_by_pos(keywords.word_set)

        pos_synsets_rm = gs.remove_terms(
            pos_synsets, 
            word_filter
        )
        pos_synsets_rm = gs.remove_terms(
            pos_synsets_rm, 
            synset_filter, 
            issynset=True
        )

        synsets = gs.find_hypo_for_all_synsets(pos_synsets_rm)

        self.synsets = synsets



word_list = pd.read_csv('../word_lists/key_words.csv')
keywords = KeyWords(list (word_list['WORDS']))
keywords.normalize_words()
keywords.include_synonyms()



class Review:
    """
    Class for storing information of a single review.
    """

    def __init__(self, raw_text):
        """
        :param raw_text: the unmodified review
        :type  raw_text: str
        :param normalized_text: text after normalization
        :type  normalized_text: str
        :param all_word_freq: keys are words, values are freq
        :type  all_word_freq: dict
        :param key_word_freq: keys are keywords, values are freq
        :type  key_word_freq: dict
        """

        self.raw_text = raw_text
        self.normalized_text = ''
        self.all_word_freq = {}
        self.key_word_freq = {}
        #self.rating = rating
        #self.time = time

    def count_word_freq(self, keywords):
        """
        Count the frequency of each individual word, split by spaces.
        Then count the frequency of each keyword.

        :param keywords:
        :type  keywords: set
        """

        # key_word_freq is not a subset of all_word_freq
        # this is because key_word_freq may include spaces in them
        # all_word_frequency does not
        self.all_word_freq = Counter(self.normalized_text.split())

        key_word_freq = {}
        for keyword in keywords:
            key_word_freq[keyword] = self.normalized_text.count(keyword)
        self.key_word_freq = key_word_freq


class Business:
    """
    Class for containing the information of a single business

    """

    def __init__(self, name):
        """
        :param review_info: 
        :type  review_info: Review
        :param all_word_freq: keys are words, values are freq
        :type  all_word_freq: dict
        :param key_word_freq: keys are keywords, values are freq
        :type  key_word_freq: dict
        """

        self.name = name
        self.review_info = []
        self.all_word_freq = {}
        self.key_word_freq = {}
#         self.num_reviews = num_reviews
        # will be a dict
#         self.hours_opened = hours_opened
#         self.price_range = price_range
#         self.address = address

    def find_review_info(self, reviews, keywords=keywords):
        """
        Find the review data information.

        :param reviews: a set of strings, 
                        each of which is a review
        :type  reviews: set
        :param keywords: keyword class containing keywords
        :type  keywords: KeyWords
        """

        all_reviews = []
        for review in reviews:
            review_ins = Review(review)
            review_ins.normalized_text = normalize_text(review_ins.raw_text)
            review_ins.count_word_freq(keywords.word_set)
            all_reviews.append(review_ins)
#         self.review_info = set(all_reviews)
        self.review_info = (all_reviews)

    def aggregate_word_freq(self):
        """
        Combine all the word count for each review
        """

        all_dict = defaultdict(list)
        for review_info in self.review_info:
            for key, value in review_info.all_word_freq.items():
                all_dict[key].append(value)

        for k, v in all_dict.items():
            all_dict[k] = sum(v)

        self.all_word_freq = all_dict

        keyword_dict = defaultdict(list)
        for review_info in self.review_info:
            for key, value in review_info.key_word_freq.items():
                keyword_dict[key].append(value)

        for k, v in keyword_dict.items():
            keyword_dict[k] = sum(v)

        self.key_word_freq = keyword_dict

    def quick_aggregate(self, reviews, keywords=keywords):
        """
        Aggregate word counts all at once, 
        and not review by review

        :param reviews: set of reviews, each of which is a string
        :type  reviews: set
        :param keywords: keyword class containing keywords
        :type  keywords: KeyWords
        """

        all_reviews = ' '.join(reviews)
        all_reviews = normalize_text(all_reviews)

        self.all_word_freq = Counter(all_reviews.split())

        key_word_freq = {}
        for keyword in keywords.word_set:
            key_word_freq[keyword] = all_reviews.count(keyword)
        self.key_word_freq = key_word_freq





