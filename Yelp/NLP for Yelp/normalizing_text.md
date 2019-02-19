# Word Search

The English language is increbily complicated, making it very important to normalize (or standardize words) for more efficient analysis.

I will also describe how I will search through the words.


# Preliminary Normalization

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

## Key word normalization

This normalization is just in case the keywords are able to be found in the text. 

1. Lowercase the words.
2. Lemmatize the words.

**Things I Still Have Trouble With**

* Abbreviations/ Acronyms. 
    * Very hard to do because it is incredibly difficult for computers to interpret what the abbreviations refer to. This is even made harder by the fact that different terms refer to the same abbreviation.
    * Also, [Google Cloud Natural Language](https://cloud.google.com/natural-language/) doesn't even deal with abbreviations/ acrynyms.
* Referential Pronouns
    * “This art is amazing. It is very inspiring.”
    * If we count the frequency of the word "art", we would only be able to pick up 1. However, the word "it" is referring to the word "art", so we should really be counting the frequency of "art" as 2.
* Unintended word usage meaning.
    * Words like "hip" can have drastically different means when used in different contexts. 

**Things To Keep In Mind**

* Should decode the text to UTF-8.

# Word Search

Ways to search for the number of appearances.

1. Delete all stop words.
    * Since we are going to be iterating over the same string, things would go faster if we delete words that we know are not going to be searched.
    * Stopwords simply refer to common English words like "I", "me", "he", "she".
* Regular search after normalizing everything. This will output a dictionary that maps each searched term to a number that describes

**Things To Keep In Mind**

* I want to be able to search for terms and not just singular words.
* Searching may take forever in Python. I might have to write this code in C.
    * If I write the code in C, here would be the steps: 
        1. Open up the file as a string.
        2. Search for number of appearances in the string.
        3. Write to a json file a dictionary mapping a searched term to its frequency.
        4. Open the json file into Python.
* To make sure things go as fast as possible, take a small sample of the text of words, run my function, time how long it takes for the function to run. Try to rewrite the function, and time how long it takes. It is important for me to do this because the dataset will be incredibly large.
* To make searching and normalization go even faster or if we cannot load all the text into memory at once, we can split the text files into chunks, and run the program for each chunk. Then aggregate all the findings.


