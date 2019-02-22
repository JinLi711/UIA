# Outline Of Goals

This is my plan for Yelp analysis.

1. Gather Data from Yelp
2. Normalize the text
3. Count frequency of words
4. Insert data into merge file
5. Find correlations.




# Gather Data

Data will come from Dan Silver's scrape of Yelp cafes. This will come: EVENTUALLY.

Things To Note:
* No clue what the file format is going to look at nor do I know what exactly is going to be in the data. I just know there will probably be reviews inside the data.




# Preliminary Normalization

The English language is increbily complicated, making it very important to normalize (or standardize words) for more efficient analysis.


## Input Text Normalization

This is the normalization step that would be (most likely) common to all of our preprocessing methods.


Lets start with the sentence:

* “This food is amazing! Why did it only cost me 5 dollars? It's greatl.”

1. Lowercase all the words.
    * “this food is amazing! why did it only cost me 5 dollars? it's greatl.”
    * Drawbacks:
        * uppercase can be used by reviewers to show emotions

2. Replace numbers with [NUM].
    * “this food is amazing! why did it only cost me [NUM] dollars? it's greatl”

3. Replace !~`#$%^&*()_+={}[]|;:"<>,.?@-\/' with spaces.
    * “this food is amazing why did it only cost me [NUM] dollars it s greatl”
    * Note that this step deals with contractions with words that we are searching for.
    * However, this will split up some words. For example, if we have hyphenated words, we will interpret as two seperate words. For example, "sugar-free" becomes "sugar free", and this will be interpreted as two different words.

4. Remove Diacritics.
    * Here's the [definition](https://en.wikipedia.org/wiki/Diacritic) of a diacritic.
    * example: naïve, entrée, pâté. Convert to naive, entree, pate.
    * Change the diacritic to whatever letter is the closest.

5. Fix the grammar of words
    * “this food is amazing why did it only cost me [NUM] dollars it s great”
    * This can be done with existing python libraries. However, I would have to look deeply into how exactly this grammar fixing.

6. Lemmatize the words
    * “this food is amazing why did it only cost me [NUM] dollar it s great”
    * this turns plurals into singulars, changes the verbs to normal present tense. Removes prefixes and suffixes basically.
    * Note that this may shift the meaning of the word. For example, the word "unhappy" would be converted to "unhappy".

7. Replace all delimiters with spaces. 
    * For example, '\n', '\t'.
    * These delimiters are interpreted as spaces (newline, tabs) 


## Key word normalization

This normalization is just in case the keywords are able to be found in the text. Note that these key words will be in a csv file seperated by newlines. The top row will include the word: WORDS

For example, here's what a [sample file](https://github.com/JinLi711/UIA/blob/master/Yelp/NLP%20for%20Yelp/Word_Lists/bohemian_words.csv) would look like

1. Lowercase the words.

2. Lemmatize the words.

To be extra careful, we should check if any of the word is misspelled.


## Things I Still Have Trouble With

* Abbreviations/ Acronyms. 
    * Very hard to do because it is incredibly difficult for computers to interpret what the abbreviations refer to. This is even made harder by the fact that different terms refer to the same abbreviation.
    * Also, [Google Cloud Natural Language](https://cloud.google.com/natural-language/) doesn't even deal with abbreviations/ acrynyms.

* Referential Pronouns
    * “This art is amazing. It is very inspiring.”
    * If we count the frequency of the word "art", we would only be able to pick up 1. However, the word "it" is referring to the word "art", so we should really be counting the frequency of "art" as 2.

* Unintended word usage meaning.
    * Words like "hip" can have drastically different means when used in different contexts. 

## Things To Keep In Mind

* Should decode the text to UTF-8.





# Word Search

Ways to search for the number of appearances.

1. Delete all stop words.
    * Since we are going to be iterating over the same string, things would go faster if we delete words that we know are not going to be searched.
    * Stopwords simply refer to common English words like "I", "me", "he", "she", etc.

2. Regular search for key words after normalizing everything. This will output a dictionary that maps each searched term to a number that describes the frequency of the appearance of the word.

3. Search for all frequencies of linking hyponyms. Note that to do this, we need to manually filter out hyponyms that are loosely related.

4. Run the raw text through Google Cloud Natural Language for entity analysis. See [here](https://cloud.google.com/natural-language/). This will mainly be used to categorize proper nouns.

## Things To Keep In Mind

* I want to be able to search for terms and not just singular words.

* Searching may take forever in Python. I might have to write this code in C.
    * If I write the code in C, here would be the steps: 
        1. Open up the file as a string.
        2. Search for number of appearances in the string.
        3. Write to a json file a dictionary mapping a searched term to its frequency.
        4. Open the json file into Python.

* To make sure things go as fast as possible, take a small sample of the text of words, run my function, time how long it takes for the function to run. Try to rewrite the function, and time how long it takes. It is important for me to do this because the dataset will be incredibly large.

* To make searching and normalization go even faster or if we cannot load all the text into memory at once, we can split the text files into chunks, and run the program for each chunk. Then aggregate all the findings.

* I also have to make a new data field that considers the total word count (since results will be skewed if appearances are higher simply because there are more reviews or more words)
    * I should think of other ways to extract information from text. For example, find the variance of the words.




# Data Structures

Not as familar with C as I am with Python, but given how large the data is going to be, it would be much faster to implement the code in C. I'm only going to use C for searching algorithms. I will just write out the results of the search into a file, then read the file with Python (and do data analysis with Python).

## Layout of Data

Haven't seen the data, but I have a vague impression of how it is going to be formated. I'll describe it ground up.

1. The lowest level would probably just be the individual businesses. 
2. The next level would be businesses in each zip code.
3. Next level would be the state.
4. Top level would the country.




# Inserting Data

So by the end, we will have a file (probably a json file) that maps each business to its information. 

We can do another level of aggregation to combine businesses together to the zip code level.




# Find Correlations

## Geographical Weighted Regression

For each variable of interest from the merge file, correlate it with the data from the json file.






