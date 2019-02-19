# Normalizing Text

The English language is increbily complicated, making it very important to normalize (or standardize words) for more efficient analysis.


## Preliminary Normalization

This is the normalization step that would be (most likely) common to all of our preprocessing methods.

**NOTE:** ["XXX", "YYY", "ZZZ"] indicates a list, "XYZ" indicates a string. 

Lets start with the sentence:
  * “This food is amazing! Why did it only cost me 5 dollars?”

Substeps:
a)	Lowercase all the words.
i)	“this food is amazing! why did it only cost me 5 dollars?”
b)	Replace numbers with [NUM].
i)	“this food is amazing! why did it only cost me [NUM] dollars?”
c)	Tokenize into sentences.
i)	[ [“this”, “food”, “is”, “amazing!”], [“why”, “did”, “it”, “only”, “cost”, “me”, “[NUM]”, “dollars?”] ]
d)	Replace punctuations and other non-letter characters: ()!@%^&-+\$.,?*"#
i)	[ [“this”, “food”, “is”, “amazing”], [“why”, “did”, “it”, “only”, “cost”, “me”, “[NUM]”, “dollars”] ]
e)	Lemmatize the words.
i)	[ [“this”, “food”, “is”, “amazing”], [“why”, “did”, “it”, “only”, “cost”, “me”, “[NUM]”, “dollar”] ]
ii)	The only change here is from dollars to dollar. Lemmatization just refers to removing tenses. For example, “cars” becomes “car” and “flew” becomes “fly”.
f)	Count word frequencies. 
i)	In this case, the frequency for each word would be one.
