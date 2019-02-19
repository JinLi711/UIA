# Normalizing Text

The English language is increbily complicated, making it very important to normalize (or standardize words) for more efficient analysis.


## Preliminary Normalization

This is the normalization step that would be (most likely) common to all of our preprocessing methods.

**NOTE:** ["XXX", "YYY", "ZZZ"] indicates a list, "XYZ" indicates a string. 

Lets start with the sentence:
  * “This food is amazing! Why did it only cost me 5 dollars? It's great.”

1. Lowercase all the words.
  * “this food is amazing! why did it only cost me 5 dollars? it's great.”
  * Drawbacks:
    * uppercase can be used by reviewers to show emotions

2. Replace numbers with [NUM].
  * “this food is amazing! why did it only cost me [NUM] dollars?”

3. Replace !~`#$%^&*()_+={}[]|;:"<>,.?@-\/' with spaces.
  * “this food is amazing why did it only cost me [NUM] dollars it s great”
  * Note that this step deals with contractions with words that we are searching for.

4. Lemmatize the words
  * “this food is amazing why did it only cost me [NUM] dollar it s great”
  * this turns plurals into singulars, changes the verbs to normal present tense.
5. 
 

**Things I Still Have Trouble With**
  * Abbreviations. 
    * Very hard to do because it is incredibly difficult for computers to interpret what the abbreviations refer to. This is even made harder by the fact that different terms refer to the same abbreviation.
    * Also, [Google Cloud Natural Language](https://cloud.google.com/natural-language/) doesn't even deal with abbreviations.
