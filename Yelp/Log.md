# Log Version 1

This is a continuition of the old log, which can be found [here](https://github.com/JinLi711/UIA/tree/master/Notes%20and%20Record%20Files). 

# January 24, 2019

Brief write up on background and objectives.
It would be a good idea to list all possible approaches that we want to try (and to sum up my write ups)

## Broad Objective: 

Try to analyze the type of neighborhood of locations. Locations can refer both to a global sense(like cities or zip codes), or a local sense (like businesses)

One of the ways we are trying to do that is by looking at Yelp reviews, as we think that Yelp can provide a lot more information about the culture of the place than we think (as people usually just associate Yelp reviews with food).

## Background

Types of neighborhoods:

1. Traditional / Neighborly/ Local type
  * the average place for average people to visit.

2. Corporate / Utilitarian type
  * practical places.
  * places where suits and ties meet.
  * places where students study.
  * think of like chains of cafes like Starbucks.

3. Bohemian type
  * places where "rebels" (nonconformists hang out)
  * supportive of diversity (ethnic, racial, gender, sexuality)

## Summary of My Research Before

I made a write up on word embedding before and pipeline for analysis, which can be found [here](https://github.com/JinLi711/UIA/tree/master/Notes%20and%20Record%20Files). (The file name is called Visual Representation Write Up).



## My more specific goals

What I'm doing is very different from what everyone else is doing. FAUI is more of a sociology group that uses qualitative analysis to understand demographics. I, on the other hand, an providing the quantatitive side. I've already done some of the analysis below in Possible Approaches to Analysis on Word. 

So how can I analyze Yelp to provide meaningful insight to the types of neighborhoods?

### Possible Approaches to Analysis on Words

1. Given a predefined list of words, find the frequencies of those words in Yelp. 
  * Why this technique?
    * Using our intuition and experience, we can hypothesize that certain words that appear more often can correlate with the type of neighborhood.
  * Pros:
    * easy to do
    * human judgement is used to decide the words. 
  * Cons:
    * we are not using the full capacity of the information in Yelp reviews.
    * there might be words on Yelp that we never thought of that can strongly correlate with the type of neighborhood.
    * Different words have the same meaning and a word can have multiple meanings

2. Build a clustering algorithm to cluster words that have similar meaning
  * Why this technique?
    * To be able to visualize words on a scatterplot (I wrote more about this on the previous log)
  * Pros:
    * we take care of the issue of different words having the same meaning

3. Create a graph/web connecting a word to other words, and finding the frequencies of each connection.
  * Why this technique?
    * Take care of the possibility of missing frequencies of words that mean the same thing.
  * Cons:
    * we're bounded by predefined words (since those predefined words act as the starting node). There's a possibility that the web may not touch words that strongly correlate with neighborhood types

### Questions I Want To Answer

1. How can I extract more meaning from Yelp reviews?
  * Right now, I'm only looking at words by themselves, and I want to eventually be able to look at and understand words through groupings.

### Current Objective

1. Find a way to create a graph to connect starting words to words with closest meaning.

# January 25, 2019

1. Did some research on possible ways of finding synonyms.

  * [Learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank). Essentially a machine learning method for ranking which infomation is the most important or relevant.
    * Decided not to look into this because there are way better methods. This is here just in case I want to look into it again.

  * Word2Vec Embedding
    * [Tensorflow](https://github.com/tensorflow/tensorflow/tree/r1.10/tensorflow/examples/tutorials/word2vec) example of Word2Vec

  * [How to use machine learning to find synonyms](https://medium.com/@nikhilbd/how-to-use-machine-learning-to-find-synonyms-6380c0c6106b)
    * Candidate Generation
      * Generate all possibilities of synonyms
      * need acrynoym expansion (like CS to computer science)
      * use Word2Vec embedding
      * use historical user data (if a person searched shoes then searches sneakers afterwards, we can assume there might exist an association)
      * Use a pre-existing lexical synonyms. Ex. [WordNet](https://wordnet.princeton.edu/).
    * Synonym detection
      * use supervised learning

  * [WordNet](https://wordnet.princeton.edu/) from Princeton.
    * Sort of used like a thesarus
    * Avaliable on Python NLTK
      * [Wordnet with NLTK](https://pythonprogramming.net/wordnet-nltk-tutorial/)
    * Not entirely extensive because 

  * [Sketch Engine](https://www.sketchengine.eu/price-list/). 
    * For language exploration that ranges from translation to text analysis to creating lexicons. Does cost money but has a 30 day free trial. 

  * [Playing with word vectors](https://medium.com/swlh/playing-with-word-vectors-308ab2faa519).
    * Python code for Word2Vec and finding similarities. Will check out next week.

  * [Get Busy with Word Embeddings – An Introduction](https://www.shanelynn.ie/get-busy-with-word-embeddings-introduction/). I know most of this, but quite a good article to reread

  * I also [stared](https://github.com/JinLi711?tab=stars) a lot of repositories on NLP. Should check those out.


**Thoughts** After doing some preliminary research, I think it would be a good idea to take the set of words that Hyesun created, and run them through Stanford's GloVe. Then try to find closest words with the cosine similarity (since words are just vectors). Another good thing to do is run the list of words through NLTK's WordNet to find similar words. Will need to look into that. Then for each similar words, find the frequencies of those words.

# January 27, 2019

1. Did research on WordNet and how to use it with Python. Also tried out some examples.

  * [Dive into WordNet with NLTK](https://medium.com/parrot-prediction/dive-into-wordnet-with-nltk-b313c480e788).
    * NLTK module contains: 
       * 155,287 words
       * 117,659 synonym sets
    * synset (aka "synonym set"): collection of synonyms
    * lexical relations:
        * Hyponym: more specific concept (motorcar is a more specific car)
        * Hypernym: a more general concept (car is a more general motorcar)
        * Meronyms: components of items (tree contains a stump, leaves, trunk)
        * Holonyms: membership to something (atom is a member of a molecule)
        * Entailment: how verbs are involved (eat involves chewing)
    * we can find the common hypernym between two words (vehicle is the common hypernym between limo and truck)
    * can also measure how specific a word is by analyzing its depth in a hierachy
    * wordnet can measure how similar two words are by finding the shortest path between them. Outputs:
      * range (0,1) (0 no similarity, 1 perfectly similar)
      * -1 (no common hypernym)
    * Example of WordNet Hierachy:
      * ![WordNet Tree](http://www.cs.princeton.edu/courses/archive/spring07/cos226/assignments/wordnet-fig1.png)

  * [Word Net Interface With NLTK in Python](http://www.nltk.org/howto/wordnet.html)
    * Contains python code for each possible function in the module

2. Created a plan for how to use NLTK WordNet to find synonyms.
    1. Combine all the csv files (which contains words for each neighborhood type) into a set of words.
    2. Lower case all the words
    3. Split the words into nouns, adjectives, and verbs.
    4. For each word:
        1. Run it through Morphy. This just helps normalizes the word to make sure the word is inside WordNet.   
        * For example, running denied through Morphy returns deny. 
        * Keep both input and output.
        2. Run the resulting word through wn.synset to find all the synsets. 
        * Keep in mind that some words have multiple definitions, and thus have more than one synset. For example, printer can mean a person who prints or a machine that prints.
        * Also note that a word may have an empty synset, meaning that word is not in WordNet. In that case, make a note.
        3. For each synset, find all its hyponyms using .lemmas(). Find all hyponyms of those hyponyms and repeat.
        * Help from [StackExchange](https://stackoverflow.com/questions/15330725/how-to-get-all-the-hyponyms-of-a-word-synset-in-python-nltk-and-wordnet)
        4. For each extra word found, find all meronyms (both part and substance)
        5. Find the depth of each word.
    5. Create a path similarity matrix where columns are the starting words, and rows are all the words found.
        * Can try different similarity metrics.  
    6. Find common hypernyms for the words found.
    7. Create a tree using everything we found.
      * [Example for getting started](http://intelligentonlinetools.com/blog/2016/09/05/getting-wordnet-information-and-building-and-building-graph-with-python-and-networkx/)
      * Libraries:
        * [ETE Toolkit](http://etetoolkit.org/)
        * [Plotly](https://plot.ly/python/tree-plots/)
        * [NetworkX](https://github.com/networkx/networkx)
    8. Calculate frequencies of the words.