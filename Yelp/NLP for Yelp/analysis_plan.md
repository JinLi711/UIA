# Outline Of Goals

This is my plan for Yelp analysis.

1. Gather Data from Yelp
2. Normalize the text
3. Count frequency of words
4. Find correlations.
5. Insert relevant data into merge file




# Gather Data

Data will come from Dan Silver's scrape of Yelp cafes. This will come: EVENTUALLY.

Things To Note:
* No clue what the file format is going to look at nor do I know what exactly is going to be in the data. 

**Here are my guesses for what's inside**

* cafe names
* locations
* reviews (there might be a cutoff for how many reviews for each cafe)




# Preliminary Normalization

The English language is increbily complicated, making it very important to normalize (or standardize words) for more efficient and unbiased analysis.


## Input Text Normalization

This is the normalization step that would be (most likely) common to all of our preprocessing methods.


Lets start with the sentence:

* “This food is amazing! Why did it only cost me 5 dollars? It's greatl.”

1. Lowercase all the words.
    * “this food is amazing! why did it only cost me 5 dollars? it's greatl.”
    * Drawbacks:
        * uppercase can be used by reviewers to show emotions. For example: "THIS FOOD IS GREAT"

2. Replace all numbers with space.
    * “this food is amazing! why did it only cost me dollars? it's greatl”
    * I do this because I'm a bit concerned that people will place numbers right next to words. For example, a person may write "8dollars".

3. Replace !~`#$%^&*()_+={}[]|;:"<>,.?@-\/' with spaces.
    * “this food is amazing why did it only cost me dollars it s greatl”
    * Note that this step deals with contractions with words that we are searching for.
    * Drawbacks
        * This will split up some words. For example, if we have hyphenated words, we will interpret as two seperate words. For example, "sugar-free" becomes "sugar free", and this will be interpreted as two different words.

4. Remove Diacritics.
    * Here's the [definition](https://en.wikipedia.org/wiki/Diacritic) of a diacritic.
    * example: naïve, entrée, pâté. Convert to naive, entree, pate.
    * Change the diacritic to whatever letter is the closest.

5. Fix the misspelling of words
    * “this food is amazing why did it only cost me [NUM] dollars it s great”
    * This can be done with existing python libraries. However, I would have to look deeply into how exactly this grammar fixing works.
    * Drawbacks
        * Intentional Misspelling Of Words. For example: "gr8t", "boi". This isn't rare in Yelp, but may actually happen.
        * Highly unlikely that misspelling correction is comprehensive. There probably are words that are correctly spelled but not recognized by the algorithm. The alogorithm may try to change the word into some other word that already exists.
        * Correcting misspelling may not lead to the correct word.
    * Note I might have to move this step closer to the beginning because some misspelling algorithms depend on the context of words (which I basically destroy with text normalization). 

6. Lemmatize the words
    * “this food is amazing why did it only cost me [NUM] dollar it s great”
    * this turns plurals into singulars, changes the verbs to normal present tense. Removes prefixes and suffixes basically.
    * Note that this may shift the meaning of the word. For example, the word "unhappy" would be converted to "happy".
    * Also note that I'm not sure if this is able to deal with compound words (or if we even want to deal with compound words). Example of a compound word: moonlight.

7. Replace all delimiters with spaces. 
    * For example, '\n', '\t'.
    * These delimiters are interpreted as spaces (newline, tabs) 


## Key word normalization

This normalization is just in case the keywords are able to be found in the text. Note that these key words will be in a csv file seperated by newlines. The top row will include the word: WORDS

For example, here's what a [sample file](https://github.com/JinLi711/UIA/blob/master/Yelp/NLP%20for%20Yelp/Word_Lists/bohemian_words.csv) would look like.

1. Lowercase the words.

2. Lemmatize the words.

To be extra careful, we should check if any of the word is misspelled.


## Things I Still Have Trouble With

I know that these may sound irrelevant, but in the context of analyzing (possibly) hundreds of millions of words, these ideosyncracies really ADDS up.


* Abbreviations/ Acronyms. 
    * Very hard to do because it is incredibly difficult for computers to interpret what the abbreviations refer to. This is even made harder by the fact that different terms refer to the same abbreviation.
    * Also, [Google Cloud Natural Language](https://cloud.google.com/natural-language/) doesn't even deal with abbreviations/ acrynyms.

* Referential Pronouns
    * “This art is amazing. It is very inspiring.”
    * If we count the frequency of the word "art", we would only be able to pick up 1. However, the word "it" is referring to the word "art", so we should really be counting the frequency of "art" as 2.

* Unintended word usage meaning.
    * Words like "hip" can have drastically different means when used in different contexts. 

* Mis-interpretation of Words in Context.
    * This is especially relevant for negations.
    * Say we are counting frequencies of the word meeting, and we have the sentence: "We are not meeting here". Would it make sense to count the frequency of meeting in this context? It really does not.

* Forgetting To Space
    * Very hard to detect if a person forgot to place a space between two words. For example: "becauseof".


## Things To Keep In Mind

* Not entire sure what text format that we are looking at, but should decode the text to UTF-8.

* I know that many platforms allow emojis: are there emojis in Yelp?





# Word Search

Note that I will do searching for one business at a time (the plan below applies for one business at a time). We can analyze data aggregations afterwards.

1. Aggregate all the reviews of a cafe together (place all reviews in one long string).
    * For example, if there are two reviews:
        * "This is great!"
        * "This is terrible!"
    * The results would be:
        * "This is great! This is terrible!"

2. Delete all stop words.
    * Since we are going to be iterating over the same string, search algorithms would go faster if we delete words that we know are not going to be searched.
    * Stopwords simply refer to common English words like "I", "me", "he", "she", etc. 

3. Regular search for key words after normalizing everything. This will output a dictionary that maps each searched term to a number that describes the frequency of the appearance of the word.
    * Example: "I really really love apple." We want to search for words "really" and "apple".
    * Output:
        {
            "really": 2,
            "apple": 1
        }

4. Write another algorithm that outputs word counts for all possible words. Note that I do not do this before the regular search because this will not allow me to search for phrases that are seperated by spaces.
    * Example: "I really really love apple."
    * Output:
        {
            "i": 1,
            "really": 2,
            "love": 1,
            "apple": 1
        }

5. Find all linking hyponyms.
    * Note that to do this, we need to manually filter out hyponyms that are loosely related.
    * I already built the algorithm that generates hyponyms. It's file output is exactly the same as the format of the keywords.
    * I have also built an algorithm to help make filtering words a whole lot easier.
    * I also made the output of that algorithm words and not phrases. This means that "cotton candy" will never appear, because it is seperated by a space. 

6. Go through the json file created to find appearances of these hyponyms.

7. Run the raw text through Google Cloud Natural Language for entity analysis. See [here](https://cloud.google.com/natural-language/). 
    * This will mainly be used to categorize proper nouns.
    * Note sure if this step is neccesary because the categories of GCP NL are way too general too be useful for us. However, this can still be an option if I have time.
    * Note that it would be best to run the raw text, and not the normalized text.

8. Aggregate all the businesses into two json file, the first being the frequencies of key word search of all the businesses, the second being frequencies of all words of all businesses.

Example:

{
    
}

## Things To Keep In Mind

* I want to be able to search for terms and not just singular words.

* Need to make the code as general as possible.

* To make sure things go as fast as possible, take a small sample of the text of words, run my function, time how long it takes for the function to run. Try to rewrite the function, and time how long it takes. It is important for me to do this because the dataset will be incredibly large.

* To make searching and normalization go even faster or if we cannot load all the text into memory at once, we can split the text file(s) into chunks, and run the program for each chunk. Then aggregate all the findings. 
    * Don't know the specific steps for this because not sure how the file format would look like yet.

* I also have to make a new data field that considers the total word count (since results will be skewed if appearances are higher simply because there are more reviews or more words)
    * I should think of other ways to extract information from text. For example, find the variance of the words.
    * For word count, should I count before normalization or after? I think I should have the word count be after normalization.

* I need to document my code very well and create test cases. Acknowledge to Professor Clark that it would take longer than my usual speed because of testing. Say its better carefully done than quickly.


* Searching may take forever in Python. I will write this code in C, but analyze the results in Python.
    * If I write the code in C, here would be the steps: 
        1. Open up the file as a string.
        2. Search for number of appearances in the string.
        3. Write to a json file a dictionary mapping a searched term to its frequency.
        4. Open the json file into Python for analysis.




# Data Structures

Not as familar with C as I am with Python, but given how large the data is going to be, it would be much faster to implement the code in C. I'm only going to use C for searching algorithms. I will just write out the results of the search into a file, then read the file with Python (and do data analysis with Python).

But note that if I implement the code in C, I'm worried that I will be unable to do more complex analysis on words to extract more meaning. 

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






