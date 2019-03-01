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
      * Note that a word can have different parts of speeches.
    4. For each word:
        1. Run it through Morphy. This just helps normalizes the word to make sure the word is inside WordNet.   
          * For example, running denied through Morphy returns deny. 
          * Keep both input and output.
        2. Run the resulting word through wn.synset to find all the synsets. 
          * Keep in mind that some words have multiple definitions, and thus have more than one synset. For example, printer can mean a person who prints or a machine that prints.
          * I might need to manually filter out words that do not meet the appropriate definitions that I want.
          * Also note that a word may have an empty synset, meaning that word is not in WordNet. In that case, make a note.
        3. For each synset, find all its hyponyms using .hyponyms(). Find all hyponyms of those hyponyms and repeat.
          * Help from [StackExchange](https://stackoverflow.com/questions/15330725/how-to-get-all-the-hyponyms-of-a-word-synset-in-python-nltk-and-wordnet)
          * Note that if the hyponym is a phrase, remove it.

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

# January 28, 2019

1. Actually was able to implement what I wrote down (see January 27). 
2. Started to do some manual filtering (since some synsets found have definitions that we do not need)

# January 29, 2019

1. Finished filtering words
2. Found all synonyms for starting words and placed information into a well formated file

# February 6, 2019

1. Possible keywords to look at:
  * music
  * time
  * night life
  * senior
  * organic

# February 7, 2019

1. I listened to the recording that Professor Clark sent. Next steps:
  * I need to take a step back and think more about how we can connect what I find in Yelp with variables that currently exist in Scenes Scape. Education? Counties? Bohemian? Cleaveages in Bohemian culture (where and why)? Time of day?
  * Read up on what Ying Cai has been doing on grographically weighted regression. (How can I use similar methodologies?)
  * Find a larger Yelp data set.

2. Read through Ying Cai's Thesis proprosal.
  * Events and activities shapes the cultural and moral dimensions of a scene.
  * I think we can do something very similar with Yelp reviews and frequencies of words.

3. Multilevel Modeling
   -	[Wiki](https://en.wikipedia.org/wiki/Multilevel_model)
   -	Multilevel modeling is like linear regressions, but it is extended to different hierarchies.
   -	Attributes that we are comparing can be nested in other attributes that we are comparing. For example, we can be comparing political engagement under the hierarchy of geographical locations.
   -	We use this method when we decide that a current model does not contain independent results, we want to compare groupings

4. Geographically Weighted Regression
   -	[Spatial Analysis](https://en.wikipedia.org/wiki/Spatial_analysis#Spatial_regression)
   -	[A spatial analysis](https://www.mailman.columbia.edu/research/population-health-methods/geographically-weighted-regression) technique that models local relationships between variables and outcomes
   -	Is basically ordinary least square regression (OLS) but extended to encompass locality (meaning it creates an OLS for each location

5. Blalock Paper Notes
    -	Pictoral Models uses arrows and boxes to imply causation
    -	Variables in boxes and lines were labeled with either (+) or (-)
    -	I can’t really tell why some lines are dotted while other lines are dark (maybe darker lines imply higher correlation?)
    -	Arrows can be multi-directional (one box can connect to multiple boxes)
    -	We can even have loops
    -	Can label the difference between the main theory and the auxiliary theory

6. My words that I can think up of:

  * architecture
  * entertainment
  * ambience
  * plaza
  * park
  * shop
  * laptop
  * office

7. Skimmed Andrew's Log.
  * Variables to consider:
  * income, neighborhood, growth, population, crime, density, cafes, time, buzz
  * Great ideas, but I don't have time to look over everything

# February 8, 2019

  * Email to Andrew
    * ME:
    >> Hi Andrew,

    >> It's Jin from Scenes with professor Terry Clark.

    >> Since we're approaching the same problem but with different backgrounds, I think it would be a great idea for us to talk about how we can use Yelp data for connections to Bohemian culture.

    >> I'm more of a programmer and a statistician than a sociologist, and I know you provide a lot more qualitative insight into these connections. I, on the other hand, can help you with looking at data and finding the techniques to measure these qualitative connections.

    >> If you would be interested in talking, replying would be great.

    * ANDREW:

    >> Hi Jin,

    >> For sure, I think it would be great to synthesize our skills in order to reach new conclusions. I haven't been specifically looking at Yelp's connections to Bohemian culture, but would you be able to give me some more specifics on what you and Ben are doing with regards to Yelp? If I recall correctly, I know you guys came up with a sort of style analysis program to classify types of art and maybe even music? Anyways, if there's any way I could be of use to you, let me know and I will try to think of something. Looking forward to hearing back from you.

    * ME:

    >> In terms of what me and Ben are doing, we're trying to build a model that can take in a mural and analyze some of its features using machine learning (like style and mood). We've put some thought into the style, but we felt that murals didn't really have a very well defined style, so we decided to focus on mood. Some of the moods that we are hoping to capture are anger, awe, disgust, fear, sadness, excitement, contentment, and amusement.

    >> Once we build this model, we hope to run the model through different murals in the city. We would get a score (or rating) that describes how strong each emotion is for each mural. Each mural would have a geographical location tied to it, and we think that it would be useful to tie these emotional scores to the current politics around the location of the murals.

    >> In terms of the music analysis, I'm not working on that; so you might have to ask Ben about it (but I got the impression that he's focusing more of his time on art analysis). 

    >> I would very much appreciate if you could provide us with insight about how to tie emotional ratings to the politics around a certain neighborhood. For example, what geographical variables might we want to correlate emotional ratings with? What are some of the variables that professor Clark has worked on from the scenes book?

    >> I was also curious about your insight into finding useful keywords in Yelp. What are the variables in the scenescape book that would be useful correlate with?

    >> Also, could you keep me up to date on what you've been working on? If you have theories that you want to test, but do not have the coding background, I can provide a lot of help.

    * ANDREW:
    >> That all sounds interesting; I think mood has a lot to do with the emotional energy mentioned in a few of the documents I've read, can't remember which ones off the top of my head. I think we could definitely connect emotional scores with political data, and maybe even some existing dimensional analysis.

    >> I don't know if Professor Clark has sent my log to you before, but I've attached it here in case you'd like to look at it. My recent work is concentrated in the last ~10 pages of the document so you'll have to scroll quite a bit, but I have mostly been focusing on making propositions based off Habermas and some sheets of variables I have looked at. Earlier log comments also include Scenescapes observations.

    >> Scenescapes is truly multifaceted; there's a lot detailing economic, political, cultural, and social effects. Scenes are measured across 15 dimensions, but these are correlated with many individualized variables, such as the presence of certain amenities (anything from martial arts studios to churches) or walkability in a neighborhood. Geographically, most of the data is broken down into zip codes because the compiled sources (Bizzip/YP) use them for classification. For now, I think the most useful dimensions in Scenescapes that would determine Yelp keywords are self-expression and transgressiveness, since they are the ones most correlated with Bohemian culture and cafes. With these variables, I'm thinking that some words you could use are "creative" or "innovative" for excitement maybe? The other moods, particularly the negative emotions, seem harder to capture in relation to art. Perhaps the Yelp review reactions (Useful/Funny/Cool) could provide insight as well. Hopefully this helped a little bit, I can more thoroughly address some of these concerns in my next log if that works for you. Thanks so much!

    * JIN 

    >> Where did you find from your log:

    >>	SysfileInfo.DDPFrenchCommuneAggregate2BKvars2012_clean.sav.xlsx

    >> I can't seem to find it in one drive. 

    >> Thanks for the insight! I really need help in trying to tie murals in cities with scenes dimensions.

    >> Also, do you know of any dataset that would be useful for me to check out?

    * ANDREW
    >> That file is in the Dropbox under Hyesun's folder, located in DataFiles/France_merge_file as a .sav file. Unfortunately my computer skills aren't advanced enough to do much with opening different file types efficiently, so given what I have to work with, I've only looked at about 5-6 data sets. I would really like to open MergeB-35.sav fully, but it doesn't work for me, even when I try to convert it to open in Excel; thus, I've only been able to get bits and pieces from making it a .txt. I'm guessing that this file should be useful because it's supposed to contain most, if not all, of the American variables? I've attached one on Korea too that I was able to thoroughly analyze in my log, it contains a lot of useful data too. Let me know what you think, thanks!

    * JIN
    >> 'll try to open it for you today or tomorrow. Is there anything in particular that you are looking for in the data? (I can provide just the headers or just the top few rows since the file is large)

    * ANDREW
    >>  think any trends or variables related to the social/cultural composition of a neighborhood would be interesting; for example, housing density or any dimensions (neighborliness, glamour, etc.) that stand out. I'm not able to see all of the variable names, let alone the data associated with each, so even just that basic outline would help.

    * JIN 

    >> Just heads up for R Code:

    >> library(foreign)
    >> library(dplyr)

    >> Read the data from spss
    >> mydata = read.spss("PATH_TO_FILE", to.data.frame=TRUE)

    >> Get only the column names
    >> col_names <- colnames(mydata)

    >> Get the head of the data
    >> head <- head(mydata)

    >> Write the head of the data to a csv file
    >> write.table(head,"PATH_TO_FILE2")

    * ANDREW
    >> Sure. So what I gather from the instructions and the log is that there are some missing counties for specific variables, most notably "religneg," crime rate, and non-white populations. I'm trying to figure out primarily what causes the missing variables and also what "religneg" means; right now, I think it's a combination of institutions? I'm still trying to follow up on Professor Clark's response from last night and continue working on it.

  * Email to Professor Clark
    >> Dear Professor Clark,

    >> I just want to recap on what I and Ben have done on the art project and how we can connect it with Scenes variables.

    >> So we are currently trying to build a model that can detect the emotions from a mural. 
    I've personally read a lot of literature combining machine learning and art. 

    >> I've searched on Google Scholar with key terms:
    >> "convolutional neural network" and art and emotion. The results produced about a dozen papers that were worth reading, and I read most of them (took notes on the log).

    >> But searching on Google Scholar:
    >> "convolutional neural network" and mural produced no meaningful result, indicating that what we needed to do was build a model that works for general art, and apply it to murals.

    >> After reading many papers on the possible techniques, we decided on one that we want to replicate because it was the newest one and it was built to fix the problems of all the other papers. It is also built on top of huge amounts of psychological literature involving art and emotions. I've also read a lot of papers on the psychology of emotions and how they relate to art (took notes on my log). The emotions that the model can rate are:
      * anger
      * awe
      * disgust
      * fear
      * sadness 
      * excitement
      * contentment
      * amusement

    >> Ben sent an email to the authors of the paper asking for their code and dataset. If they provide it to us, it would save a lot of time, and we can apply the code onto murals. If not, we will have to replicate the paper ourselves.

    >> So how we can connect it to scenes variables? Pulling from the meeting on Wednesday, we believe that we can use the model to rate emotional responses from murals in different geographical locations. Once we have these ratings, we can use geographically weighted regression to correlate these emotions with scenes variables and political connotations.

    >> It would be interesting to use this to see the Bohemian cleavages in different areas. 
    Tying this to the Yelp data, we can look at keywords in Yelp reviews that somehow connect to these emotions.

    >> My theories for each emotion:
    >> anger, fear, sadness: If a mural has a rating of high anger, fear, or sadness, we have to ask why. Is there a political movement of activism surrounding the mural? Are people dissatisfied with something? This leads to a natural possible test of correlation between anger and variables like income, quality of life (measured by amenities), feeling of injustice (connection to the scene's book of egalitarianism). On the opposite end, the emotion of contentment can also be linked to the same variables.

    >> awe: If a mural has a high rating of awe, it may be possible that the murals may be trying to attract visitors and tourists. This directly tied to amenities since places that try to increase tourism would likely to also have a lot of amenities. We would also expect that the location of the mural to be in a Bohemian environment.

    >> disgust: I doubt there would be any high ratings of disgust in murals, but we may be surprised. 

    >> excitement: More ties to Bohemian culture and self-expressionism.

    >> These connections with scenes variables are preliminary. I've been talking to Andrew, who I feel can provide extremely valuable insight into more of these connections.

    >> Last thing to address: why machine learning and not any other method? 
    Machine learning is the only realistic way to analyze art in a quantitative fashion. Doing a search on google scholar will show that the top results will be applying machine learning to analyze art.
    And why quantitative over qualitative?
    Because quantitative approaches are extremely scalable. If we build this and it works for a city, this model will be an incredible tool to use when trying to analyze murals globally. Furthermore, we feel that qualitative analyze is too fickle, inconsistent, and time-consuming.

    >> I'll send another email later detailing how we can use Yelp data to connect with scenes variables.

    >> Best,
    >> Jin Li

    * TNC

    >> Jin and over us,

    >> Most of all I am delighted to see the clarity and specificity in this email.  You can clearly write out the logic of what you're doing and frame it in more general terms. It is here. This is exactly what we need for others to think about how to connect with what you're doing and to comment and try to mutually help one another.  

    >> Everything is intermediary and all of these ideas are potentially useful. But how to focus a bit more on some and less on others? Just a few big points.

    >> 1. you were using to terms machine learning and convolutional neural networks. But you seem to have searched on the second not the first? Are there other keywords or variations of these it might Bring in more related efforts?  

    >> 2. if for some at least exploratory purposes we want to try more concretely immediately available data we could use some of the types of variables in our existing ZIP Code or point data for amenities, like the  Merge files that Andrew is reviewing.  These have thousands of variables ranging from cafés and Baptist churches to tattoo parlors bars museums and more more. If it would be simpler to connect the titles of some of these or data about them from some more readily available source that is already been used and Encoded by someone else– Such as bars compared to cafés or tattoo parlors–then we could use their results about how they relate to the psychological dimensions which you list here.  

    >> The psychologists dealt with hundreds and thousands of specific personality dimensions such as these emotional reactions and their frequency or intensity reported by different individuals over the entire 20th-century. Near the end of the century they decided to focus most of their work on five key dimensions which subsumed many of these that you list like anger and disgust. We have compared the scenes 15 dimensions to the five psychological dimensions in a few papers one more general representatives like a psychological meeting which is not published in the second one is it chapter draft on the Chicago oral history on the website from that book. I would not bother to try to read these in detail right now but to build on my main conclusion witches the correlations are probably something like.2 2.3 at the highest and sometimes zero. 

    >> 3. Maybe  the biggest point is very elementary statistics: if we're looking at paths or elites to be leads to seeing leads to D what is the impact of this causal set of linkages? The normal way to get a rough estimate assuming nothing else affects the causal path is to simply multiply the strength of each causal link by each of the others. So if the A to B  path is .2  and the B to C path is .2, the path from A to C is .04.  If we join this statistical logic with the philosophical logic how can we join interrelated propositions or two variables of the sort that you discuss, the point is your text often assumes a very strong relationship, which is essential for the logic to hold. But if the empirical relation is in fact week we're wasting our time very likely. 

    >> The main example. When we try to reason this way that is semi fallacious is how strong are variables like income or education or race  or gender? You've heard me say many times including yesterday Wednesday's meeting that These are interrelated in ways explain about 15% of their variance with most things in social sciences study including us, such as voting going to a café buying a car getting married etc. 

    >> I am not suggesting that we stop using these variables but do so only fully recognizing the weakness of the relationships, and build models and analyze data and look for better measures accordingly.

    >> In the case of what we're doing with most of the variables you  discuss below what we need is to spell out as you're doing here what's up linkages are logically between each of the variables and analysis steps that might follow next. This is what we're doing with our café propositions that Andrew's been extending.  Then to think what data we have and what models can be used to test them. This is what we're doing discussing the Data from our existing files as well as the new kinds of possible measures and how far a field we should go and howl loose or week the relationships are between the new work and Core control variables that we are ready know about.  You and I discussed this Wednesday after the staff meeting and recorded it in five minutes or so that I sent you. Your email here is a perfect response, permitting me to articulate some of these points and asking how they might shift any of your possible next steps?

    >> 4. the clear simple answer is that we may have nothing that is ready to join in the ways that we need to do so that will  work in a few weeks of work right now, and  we should quit or consider how to change course.  

    >> 5. but how might we shift what we are trying (as you outline) to incorporate my points? One is for you to work a bit more on actual modeling with the local area data so that you realize more precisely what we have and how it can be modeled and not do things that are unworkable in a few weeks. ’this would be great for Andrew too.  OR expliclity ask what to change, such as changing these key words or not using murals or only trying to do this for a few locations where we have richer data as a quasi case study. 

    >> 6. the biggest point is to try to articulate this in writing as you're doing now not just to dive in and waste time starting things that are not going to work for in a few weeks.  Recall what I just sent from dance over that he should be sending us some scraped yelp data from Toronto soon, so we can consider those data before long but should not try to duplicate the Toronto effort of scraping.

    * Ben Picker

    >> I am going to think out loud here. Please take any points I make with a grain of salt. I'm just thinking creatively. 

    >> The statistical work we plan to do with machine learning tools has a specific purpose. We want to take a images of murals with their addresses and use algorithms to identify what emotions occur within the murals. Once we have these emotion profile for each image, we will join this with the scenes data. 

    >> I am considering what our research focus should be. One basic question is, can the emotions expressed in mural art at specific locations be used to predict properties about their surrounding communities? 


    >> A first issue that should be addressed is whether studying emotions at a community level is valuable for understanding scenes. 


    >> Why Scenes and Emotions Should Be Related 

    >> Regarding the relationship between scenes and emotions, I need to see the specific papers you’re referencing so if you could give exact titles that would be great so I can see what approach you took. I accept in your studies, no correlation may have been found. 

    >> But the theory in my opinion doesn’t support that viewpoint. From a theoretical point of view, I find the claim that emotions and scenes won’t be correlated in some way, to be highly unlikely. It may be difficult to specify exactly how, but I am sure a relationship exists. 

    >> I am going to explain why I believe this is so. 

    >> On a basic level, emotions are what drive behaviors and, for humans, usually form the basis for artistic expression. But emotions are not unique to humans and if you observe animal communities across mammals, emotional expression from individuals affects collective decision-making significantly. 

    >> For instance, in ape species, infanticide often occurs from alpha males wishing to kill off competing offspring. In response, female apes engage in allocentric mothering, where the mothers all work together as a community to protect their children. Emotions from one female affect emotions from another and, in this more simplistic context, it is quite visible how emotions are intended to impact communities. 

    >> Social neuroscientist John Caccioppo has shown in countless publications that the feeling of “loneliness” is intended to push individuals to be part of a community. When we feel lonely, we are suppose to feel sick and unwell. It is how our bodies and brains tell us “You are in danger. You are alone. You need to find your community.” and this changes our behavior. 

    >> I could cite more evidence, but the point is emotions have strong impacts on how members of communities act and their collective decisions. 


    >> Behavioral economics has pioneered our understanding that these emotions have direct implications for decision making. A classic example is Daniel Kahneman and Amos Tversky’s 1979 Prospect Theory: An Analysis of Decision Under Risk. For example, Kahneman and Tversky found that the median coefficient for loss aversion to be 2.25 higher than reward seeking, implying people are more afraid of losing money than gaining a reward. This is a tangible example of how emotions can impact measurable economic variables like gambling behavior. 


    >> Thus, not only are certain emotions inherently designed to influence our communities, but psychologists and economists now have shown that you can measure their impact on economic variables. 


    >> The examples I presented above is behavioral microeconomics. But presumably there is behavioral macro-economics. 


    >> At a community level, we can think of communities as having collective emotions. Here is an excerpt from Collective Emotions in Conflict Situations: Societal Implications

    >> “Of special importance for us is the assumption that just as individuals may be characterized by a dominant emotion, societies, too, may develop a collective emotional orientation (Jarymowicz & Bar-Tal, 2006). This process occurs as a result of particular societal conditions, common experiences, shared norms, and socialization in a society (Kitayama & Markus, 1994). The understanding of the central role of emotions within social and political contexts, with the acknowledgment of their potential to become a societal phenomenon, leads almost naturally to their examination as part of intragroup and intergroup processes. This issue concerns the role of collective emotions in situations of intergroup conflict and peace making.” 


    >> https://pdfs.semanticscholar.org/db1b/424e6ffa0a2fd1d5416248c2d3f3e396ec94.pdf


    >> I presume there is a deeper literature on this that specify exactly how researchers have approached measuring community emotions. 


    >> Behavioral macro-economics is an emerging area of research currently attempting to incorporate principles of emotion into the way economists measure. Here is an example 

    >> We [assume] that agents experience cognitive limitations preventing them from having rational expectations. Instead, these agents use simple forecasting rules (heuristics) and evaluate the forecasting performances of these rules ex post. This evaluation leads them to switch to the rules that perform best. It can be argued that in a world of great complexity that nobody fully understands, such a process of adaptive learning might be the rational way of deal handling this complexity (Simon 1957, Gigerenzer and Selten 2002, Ackerlof and Shiller2009).

    >> This adaptive learning assumption introduced in an otherwise standard New Keynesian macroeconomic model produces endogenous waves of optimism and pessimism (animal spirits) that drive the business cycle in a self-fulfilling way. This also leads to a two-way causality. That is, optimism (pessimism) leads to an increase (decline) in output, and the increase (decline) in output in term intensifies optimism (pessimism) (De Grauwe 2012, De Grauwe and Ji 2017a).

    >> An important feature of this dynamics of animal spirits is that the movements of the output gap are characterised by periods of tranquility alternating in an unpredictable way with periods of intense movements reflecting booms and busts. Technically, this means that the distribution of the output gap and output growth is non-Gaussian and exhibits fat tails.

    >> There is now a significant body of empirical evidence showing that the output gaps (and also the growth of output) in OECD countries do not exhibit a Gaussian distribution, but are characterised by excessive kurtosis and fat tails. Fagiolo et al. (2008) and Fagiolo et al. (2009) carried out important econometric analysis documenting the non-normality of the distribution of output gaps and growth rates of GDP. Thus, our behavioural model predicts that in the real world the output gap does not follow a normal distribution, but is characterised by excess kurtosis and fat tails. This feature of the higher moments of the output gap is generated endogenously in the model. It is not the result of imposing such a feature on the stochastic shocks hitting the economy.

    >> https://voxeu.org/article/behavioural-economics-also-useful-macroeconomics 



    >> So, not only can emotions drive individual decisions, but collective emotions can perhaps explain larger trends in economic behaviors (e.g. stock crashes). 


    >> Given the above, there is no question emotions should be a useful tool in sociological analysis of communities. 

    >> Mural art as a tool for sociological analysis


    >> Both Scenescapes as well as Cristina’s chicken and egg paper and other literature support the claim that art influences economics. The presence of art jobs can affect job growth. 


    >> But part of why art matters is it inherently is emotional. Art is naturally a means for emotional expression. And therefore, if there is a correlative or causal link between jobs and economic growth, emotions should play a role. 


    >> For instance, on page 157, Scenescapes discusses walkability and its relationship to population growth.  The graph on page 158 shows clearly that (1) walkability and population growth are related and (2) local authenticity is an important conditional factor that affects this relationship. 


    >> Without question, mural art plays a role in walkability. When I walk by murals downtown, often they can be extremely attention grabbing and cause me to stop dead and admire them. Intuitively based on experience, understanding more about the content of these murals and how it affects walkability would be important then since walkability is related to population growth. 


    >> It also presumably is related to the scenes dimensions, even if a correlation hasn’t yet been determined. Scenescapes shows how the scenes dimensions offer a critical tool for sociological analysis, but they are not without limitations. It is possible the low correlations seen between scenes and emotions in the past is due to interpreting the conceptual definition of the scenes in a way that doesn’t match their operational definition (as shown in chapter 8 of Scenescapes). 


    >> In short, I think logically understanding the emotions in mural art should help us understand better the relationship between walkability and population growth. 


    >> Example: Graffiti  


    >> Depending on our definition of art, graffiti that arises as a form of vandalism and property damage could be considered a type of mural art. According to Google a mural is “a painting or other work of art executed directly on a wall.” Even if we don’t consider graffiti to be a type of mural, it’s highly likely graffiti influences how residents feel about mural art. 


    >> https://www.jstor.org/stable/pdf/3590167.pdf?casa_token=OkNJBSUQKuYAAAAA:jT_jPA4QkEF3Xk006pjGQ_dSm7sBWtwV40lgjIyw_iMyIVlCLSZJvkTrU7NLQO8Vh_kcr059cCh2XLG31rgqqU842K7WNPyYwQhkcNvewjMKlqlAV9k


    >> In this 2004 article, Steve Gibbons argues that domestic property crime such as vandalism or graffiti may motivate fear of crime in the community. The abstract states: 


    >> This paper estimates the impact of recorded domestic property crime on property prices in the London area. Crimes in the Criminal Damage category have a significant negative impact on prices. A one-tenth standard deviation decrease in the local density of criminal damage adds 1% to the price of an average Inner London property. Burglaries have no measurable impact on prices, even after allowing for the potential dependence of burglary rates on unobserved property characteristics. One explanation we offer here is that vandalism, graffiti and other forms of criminal damage motivate fear of crime in the community and may be taken as signals  or symptoms of community instability and neighbourhood deterioration in general. 


    >> Furthermore he says 

    >> Crime in urban areas has effects over and above the direct costs to victims, the costs of deterrence and the costs of law enforcement. The 'fear of crime', whilst not a uniquely urban phenomenon, seems closely related to densely populated and built environments (Bannister and Fyfe, 2001). Urban crime has, in addition, a powerful influence on perceptions of area deprivation. 


    >> One might imagine then that the content of a mural will significantly alter the perception of whether it is merely decorative or a form of “property damage.” And it may also be possibly that residence may start feeling more negatively towards murals if they perceive them to be acts of vandalism. 


    >> To understand the social impact of graffiti, consider for instance “Race, affect, and emotion: young people, racism, and graffiti in the postcolonial English suburbs.” Anoop Nayak argues that 


    >> https://journals.sagepub.com/doi/pdf/10.1068/a42177?casa_token=m5I-5mlK8zsAAAAA:Kp2o_IiJATofVmloeZHrSt0XKPNK9QK-MsDUsFV_PvyZS6J0uROtqH5Ap19hnEvYJCV6hHVn2NXa



    >> Racist graffiti makes palpable a silent assumption that white working-class communities are the victims of an encroaching multiculturalism that must result in a fatal `last stand'. These emotions have a critical role to play when it comes to the feelings and resentment that surround access to public housing throughout the West Midlands conurbation. As Ahmed (2004a, page 128) recalls, ``fear does not involve the defence of borders that already exist; rather, fear makes those borders, by establishing objects from which the subject, in fearing, can stand apart''. These affects then are always in emergence, calibrated through the sediments of past histories of race that exist in the folds of contemporary English suburban dwelling. It is an exterior that we can now penetrate with a closer analysis of racist and nationalist graffiti that graphically capture how space is transformed into white territory


    >> This is just one example, but there are a bunch of papers on how graffiti influences communities. 


    >> And graffiti then would certainly influence walkability. 


    >> So, imagine the following two situations

    >> A community has murals containing more positive imagery. Residents find it uplifting and enjoyable, which improves walkability and leads to population growth. 

    >> A community has murals containing negative imagery. Residents find it fear-inducing and feel it is like graffiti, which reduces walkability and decreases population growth. 


    >> These are just some crude elementary hypothesis, but with more writing and discussion, we could build up more specific propositions that relate to Scenescapes. 


    >> We could also address some of the issues in past papers connecting scenes to emotions and try to understand why they previously failed to find a relationship between scenes and emotions since there is an abundance of evidence and literature as I mentioned earlier that indicates there should be. 

    * Terry Clark

    >> Yes these are all reasonable points. And authors dealing with very small ends will write and think more deterministically. But if we raise the N we have over the years of our research the beta. / Pearson rs declin. My main references you’ve heard me say this hundreds of times in classes is to look at the literature in any of the social science journals

    >> We can communicate more cumulatively if you address more specific points that I make which show how I go beyond the points you’re making here but don’t disagree with them

    * Ben

    >> I will reply later to your previous points in a separate email. I will address the issue of finding papers in this email. 

    >> Searching through the journals isn't turning up anything along the lines of the papers you describe.  I need more specific information to efficiently search properly. Can you give me specific titles of the papers you have in mind or the authors? Even just knowing the authors might be enough. If you're one of the authors, can you provide your co-authors? 

    >> Here are some example searches I tried
    emotion sociology correlation pearson
    https://scholar.google.com/scholar?start=10&q=emotion+sociology+correlation+pearson&hl=en&as_sdt=0,14 

    >> emotion "terry" "clark" scenes
    https://scholar.google.com/scholar?start=10&q=emotion+%22terry%22+%22clark%22+scenes&hl=en&as_sdt=0,14

    >> emotion sociology plutchik macro
    https://scholar.google.com/scholar?start=10&q=sociology+emotion++plutchik+macro&hl=en&as_sdt=0,14

    >> None of these turn up papers discussing Pearson correlations consistent with what you are saying. I went through like 10-15 for each search. 

    >> By contrast, I fairly quickly found one paper in support of using emotions in the manner I am talking about that does involve Pearson correlations with emotions and abstract categories for measuring culture.  I attached the paper. It discusses a framework that uses some author Hofstede's 4 proposed dimensions for culture classification. They categorize countries according to 4 dimensions: 
      * Power distance
      * Uncertainty avoidance
      * Individualism
      * Masculinity 
    >> In this article, they then analyzed the emotions of facial expressions in photographs of individuals from these countries. 

    >> In order to examine the effects of cultures on the perception of emotion, Pearson product-moment correlations and Spearman rank-order coefficients were computed between the two indexes of three of the four cultural dimensions and each of the emotion variables. The masculinity dimension was dropped from the analyses, since an adequate test of the hypotheses concerning this dimension would involve the testing of sex differences for each culture, and examining how the degree of sex difference relates to masculinity as a culture-level concept. All significant correlations reported for the remaining three dimensions were also significant using the rank value for each of the dimensions, and with the rank-order coefficients using the same variables. All significance tests are two-tailed.

    >> I have attached screen shots of the correlation tables. As you can see, several of the correlations are well above 0.5 in magnitude and also tested to 95% confidence. 

    >> From a methods standpoint, this study is actually similar to what we are proposing: 
    >> rather than analyzing faces, we would be analyzing paintings. Analyzing faces and paintings is remarkably similar from a machine learning perspective and emotional analysis of faces is heavily, extensively studied. Therefore, I am confident if a study like this has succeeded for facial analysis, one for mural analysis would also be plausible.   
    Rather then doing it by hand, we would use machine learning classifiers. 
    Rather that tying individuals to countries, we would tie murals to zip codes. 
    Rather than using Hofstede's dimensions, we would use your scenes dimensions. 

    >> In brief, I think this paper provides an excellent example both that (1) what I am saying is plausible theoretically and (2) that our proposed approach could work operationally since the results shown in this paper are what I am envisioning murals could do for walkability relative to scenescapes. 

    >> Of course, it will take us some time to refine testable hypotheses on paper, but both conceptually and operationally I think what Jin and I have proposed seems solid as a ballpark idea to develop into a proposal. 

    >> If you have evidence to the contrary of what I am saying, I welcome anything specific you can give me so that I can see how we are off base. But I need specific citations. 

    * Terry Clark

    >> Sorry Ben,  but you skipping the 2 main points I am making:
    >> 1. that with LOW N’s the coefficients rise, and the paper you send has N’s of about 7 to 15 I guess coders? I read thru and it does not seem  to say, referring to
    another study only for this “detail".
    >> 2. Second more critical is if we know that no ONE variable — emotion, income, race, SCENES etc — is totally deterministic, alone or combined, we need a multi causal analysis of many variables.  And if we put these in a causal chain, the impact of a more causally distant variable on subsequent variables is the PRODUCT of all the low coefficients.   But theLOGIC you and MANY people including social scientists are following ASSUMES, if you say we have NO DATA on  X but it is related to Z, and  Z is related to W, and W is related to G  then you need the product of all these coefficients to join the LOGIC. 

    >> I say this in most of my classes and many miss the point because it contradicts the media and many deterministic sounding intellectuals. “My theory says Why”. Paul Lazarsfeld did a famous paper on this called The Art of Asking Why? 1930s which still holds here.  And  it is discussed a bit more in ch 2 of the City as an Entertainment machine, p..22-33, esp. the table on p.33 which shows the LOW r’s of income, education, and race, age. Sometimes I pass this table out to all and we discuss for an hour.  Most students disagree but it takes time to get the point and internalize it. Look at the journals with N’s that are of the normal MINIMUM for comparison across variables in muticausal work:  about 1500 which is the standard low N for national citizen surveys.  N’s of 7 don't count. Yes I am unusual in making this point, but reasonable persons can be persuaded if they think and look at the evidence.

    >> I am in no Way opposed to emotion or psych variables. My BA is in Psych and I have done many studies that touch on psych variables, like citizen surveys. But my DATA and findings are NOT outliers; just look at the adjusted R2 in a  multiple regression study with 1500+ cases. The is the “common variance”. Read Hubert Blalock on causal inference in path analysis work for  empirical measures of causal sequences. 

    * Hyesun

    >> Walkability is very complex term that needs to address multitude of definitions. Measuring walkability by what dimensions? Have you read any literatures? Walkscore and other real estate tools simply measure walkability based on density of services, not considering actual pedestrian traffic or civic activities happening on the street. 

    >> Usually downtown /CBD area  is more walkable than other neighoorhoods in the city because there is more concentration of transportation, services and businesses. 
    Thus, it is hard to simply say walkability has increased due to murals because these places are already more walkable than other neighborhoods in many cities. I attended symposium at UIC last week , and there was a session where mural artists presented and talked about their methodology. One of them, Chris Devins, is actively working in Bronzeville through murals, and he blends urban planning and arts as tool of place making. His work: https://www.chrisdevinscreative.com/bronzeville-legends-initiative/
    You see those murals in Bronzeville are very expressive of historic figures related to black metropolis, Jazz, and other successful one that preexist. I think these murals that have special connection to history and roots drive more dramatic impact or changes than downtown murals that are usually less implicative but more art itself. The other mural artist, Andy Bellomo, has been working in LGBTQ communities and other underserved areas, and her works advocate social change and human rights. Those artists at the symposium also said that when mural art is commissioned in more marginalized or ethnic neighborhoods, those emotions typically become more sensible representations of communities because people can engage more in those emotions. In contrast, murals in downtown are usually commissioned for the purpose of activating commercial corridor with less political expression. They use lots of geometries, colors, objects, natures, and animals instead of actual “message” that potentially moves emotions. Of course, personally I am also big fan of murals no matter where they are, but just to differentiate their styles, murals in actual communities have distinct appearances. I think there are different types of emotions that need to be translated into different physical activities on the street level, not just one walkability or population growth. 
    For example, one of propositions could be like, "Do those murals in low income black neighborhood build more “traditional and neighborly” emotions, and attract more visitors to cafe (other existing commercial amenities) near churches?”   This is just one example to stimulate ideas. 

    >> How would you gather mural data? 
    >> I have found several sources that have list of murals, but are you planning to create a dataset based on several sources? 
    >> Or do you have one combined set already?




  * Watched this [video](https://www.youtube.com/watch?v=yPaPZDg6JAA) on how to convert spss files into .csv.
    * Basic commands in R:
      * library(foreign)
      * mydata = read.spss("C:\\Find\\Your\\File\\File.sav",to.data.frame=TRUE)
      * write.table(mydata,"mydataFormR.txt")
    * But note that conversions aren't that great (reading the converted csv into python is messy- all the rows and columns are messed up)


* 1. Reread the last pages of Andrew's log, where he looked into the variables of the merged files.
    * Building off of Andrew's log. Merged file of: •	SysfileInfo.DDPFrenchCommuneAggregate2BKvars2012_clean.sav.xlsx. I can't seem to find this in one drive.
    * 480-490: crime. It may be possible that murals with negative emotions are associated with crime in that area.
    * 526-532: sports. Still thinking about how we can find connections.
    * 535-539: cinema. Is cinema somehow related to murals? I feel like people who appreciate cinema would appreciate murals.
    * 568-580: jobs. Is it possible that positive emotions tie to jobs?
    * 935-939: music. 
    * 959-989: ethnic groups. Are there areas divided in terms of ethnic groups where mural emotional ressponses link? Maybe some ethnic groups have problems that they want to address, and they show it through murals.

  * Spent some time looking through one drive for data to build on top of.
    * Nothing here:
      * [Art scenes conference Neubauer](https://uchicagoedu-my.sharepoint.com/:f:/r/personal/tnclark_uchicago_edu/Documents/Scenes.FAUI.ReferenceFiles%20via%20App%20From%20Silver/Art%20Scenes%20Confernce%20Neubauer.No%20Vidoes?csf=1&e=aTfbLp)
      * [JElena](https://uchicagoedu-my.sharepoint.com/personal/tnclark_uchicago_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftnclark_uchicago_edu%2FDocuments%2FScenes%2EFAUI%2EReferenceFiles%20via%20App%20From%20Silver%2FArt%20Scenes%2EMaximeJElenaR).
      * [Art.Misc](https://uchicagoedu-my.sharepoint.com/personal/tnclark_uchicago_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftnclark_uchicago_edu%2FDocuments%2FScenes%2EFAUI%2EReferenceFiles%20via%20App%20From%20Silver%2FArts%2EMisc).

    * [Simplified Data](https://uchicagoedu-my.sharepoint.com/personal/tnclark_uchicago_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftnclark_uchicago_edu%2FDocuments%2FScenes%2EFAUI%2EReferenceFiles%20via%20App%20From%20Silver%2FHIstoric%2EArtsDistricts)
      * Not sure where these places are and if there's any artwork connected to it.

    * [Zips per art district](https://uchicagoedu-my.sharepoint.com/:x:/r/personal/tnclark_uchicago_edu/_layouts/15/Doc.aspx?sourcedoc=%7B351a8098-003b-4deb-b260-05c8aec4971e%7D&action=default&uid=%7B351A8098-003B-4DEB-B260-05C8AEC4971E%7D&ListItemId=34135&ListId=%7B8296D5AE-E18F-40B0-8987-917D0829EEAC%7D&odsp=1&env=prod).
      * Notable variables include:
        * population
        * analysis area
        * state 

    * [Juliet Lee LA](https://uchicagoedu-my.sharepoint.com/personal/tnclark_uchicago_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftnclark_uchicago_edu%2FDocuments%2FScenes%2EFAUI%2EReferenceFiles%20via%20App%20From%20Silver%2FLA%20CUT%2FJuliet%20Lee%2ELA).
      * Took a look into US_Merge_Hyesun.
      * 800 megabytes.
      * The [variable](https://uchicagoedu-my.sharepoint.com/:x:/r/personal/tnclark_uchicago_edu/_layouts/15/Doc.aspx?sourcedoc=%7B4E0762BA-0E8E-4E79-B563-8E5BADAAB7CF%7D&file=variablelistforJulietLee.csv&action=default&mobileredirect=true) list tells me almost nothing, so I would actually have to download and look at the data.
      * The data is very messy and difficult to handle on my computer because its large, and there's no description on the variables.

    * [This](https://uchicagoedu-my.sharepoint.com/personal/tnclark_uchicago_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftnclark_uchicago_edu%2FDocuments%2FScenes%2EFAUI%2EReferenceFiles%20via%20App%20From%20Silver%2FSPSS) may be useful to check out, but not sure which ones to look at.

    * I still can't find the dataset that Clark wanted me to find. It was something about LA and mural pictures.

  * Read the last 10 pages of Ian's Log. My thoughts:
    * is data from spotify really pheasable? How do we get data corresponding to each cafe?
    * I thought some of the videos were very interesting, though I'm not entirely sure how I can use these videos in word analysis.
    * Is it possible that in the Yelp reviews, people would actually state the genre of music? How can I find this?
    * Music key words that I can think of: pop, jazz, romantic, quiet, soft, acoustic
    * searching Yelp with terms like "Bohemian cafe" can produce valuable results (since Yelp uses algorithms that link Bohemian to words like hip and whatnot)

  * Dan Silver on Yelp data.

    >> Great idea! Right now, though, we haven’t matched the three levels together, i.e. a) venues, b) user profiles and c) reviews. That should come in the next week or so hopefully, and I’ll send it over to you when it is ready. 

    >> The MA student working on it is also this week supposed to complete a script that would enable global scraping as an automatic process (so that the scrapers respawn as they get blocked, and automatically check that they’ve got complete information for each area before moving on)…we’re going to let it loose on a sample of cities hopefully within the next couple of weeks to see how it goes.

    >> The plan is to do it in a dual way, on one side “snowballing” out from Toronto based on the cities that torontians also review, and then on the other based on sampling large, medium, and smaller cities. The idea is that if we do it this way we’ll get a good sample even if somehow on the way we get blocked in a more permanent way.

    >> Anyway, will definitely keep you updated! 

    >>We had a good discussion today of Night time and scheduling of café bar Club closing hours and asked ourselves have to measure it. first answer; lets try Yelp!

    >> times are included in our sample scraping data for one Chicago zip.

    >> Are you still working on Toronto? Could we try to play with these data if you still have not move to the national scraping?  There are too few cases to try key word searches or regression modeling, but adding NIGHT or more “business hours” for corporate area amenities should be   a good step ahead.

    >> We are also liooking for data how to capture music and images nearby like murals. 

  * Possible things to consider after looking at Yelp:
    * I noticed that sometimes business owners respond back to the reviewers. Is this a sign of professionalism and utilitarianism?
    * uses of LOL, LMFAO, mellienial acryonyms. Probably linked to Bohemianism.
    * I think its very interesting how some of the photos aren't even of food. Sometimes its something distinguishable about the place (like a hanging artwork)
    * cool
    * why are we looking at only singular words and not words in context?

  * [The City as an Entertainment Machine](https://www.dropbox.com/s/ostkfi2qjkih7h8/Full%20Book.July%202011.pdf?dl=0).

# February 8, 2019

1. Ideas About How To Interpret Text Language (and what I can do with NLTK)
    -	Think about how words are grouped together (split sentences into bigrams).
    -	Look at uncommon words, not just common ones
    -	Create frequency tables for different hierarchies (frequency under zip codes, businesses, individual reviews)
    -	Think about different ways to split the string of texts. By sentences? Paragraphs?
    -	How can I interpret ambiguity in the text? For example, how do I deal with pronouns?
    -	How can I normalize text? And what are the drawbacks of doing so? Lowercase all the text (but ALL CAPS indicate emotions). Convert all words to the same tense (flew to fly). Remove plurals (cats to cat).
    -	Tag parts of speech (but not sure how this would help yet)
    -	Convert words that have the same meaning to the same word (like happy and joyful to happy)
    -	How to deal with numbers?

2. Research Questions:
    -	How do cafes create a scene? 
    -	How can we know what “scene” is in the cafe? 
    -	What values do certain cafes in an area display (like creativity, cosmopolitanism)?
    -	How can we use that to relate to politics? 
    -	How can I add on to or contradict what has been said in the scenes book?

    -	Is there a way to distinguish which cafes/bars are more conservative/ liberal?
    -	How does time intervals of activity (cafes in afternoon vs bars at night) affect how people voice their opinions?
    -	How can I know what central themes are in certain businesses? (feminism, egalitarianism, peace, gay rights)
    -	How can location (proximity) of cafes and bars to cultural places affect political expression?
    -	How can I find cleavages (age, race, gender, religion, class) inside different bars/cafes based on Yelp data?
    -	Are there connections between what people decide to eat and their political agendas?

3. Quotes From Scenes Book:

  * These quotes are for ideas I want to address using the Yelp data. Note that page number is according to PDF.

  >> “Ambitious political programs have emerged around the world, with the character of the scene sometimes taking center stage as a topic of political controversy and target of public policy.” (page 177, Scenes)

  >> Major Claim: “Scenes grow more politically salient in general with (1) the rise of culture, (2) the rediscovery of the urbane, and (3) the new political culture.” (177)

  >> “Democratic votes were correlated with more urbane dimensions like transgression and self-expression; Republican votes, with more communitarian dimensions, like neighborliness and tradition.” (178)

  >> “Styles of political leaders and urban governance have in some cities dramatically changed, adding new cultural and aesthetic sensitivity to their past repertoires” (179)

  >> “Scenes accordingly become a topic of political contestation and a source of political authority” (179)

  >> “Scenes provide cues about the character of a place, which some people find welcoming and others find alien and strange, sorting themselves accordingly.” (182)

  >> “New Social Movements Are Typically Located in Dense, Walkable Areas with Self- Expressive Scenes and Many Artists” (195)

  >> “Where do NSMs thrive? They are usually present in high rent, high crime counties, and there are more of them in Democratic counties. Neighborhoods with any (and many) NSMs are usually in dense, lower rent zip codes with strong cultural employment concentrations, nonwhite residents, and college graduates.” (198)

  >> “When walking and self-expression come together, the result is quite likely to be organizations advocating for human rights, social justice, and the environment.” (202)

  >> “self-expressive scene, for instance, likely indicates a broadly culturally liberal environment” (206)


  >> Scenes have been rising.

  >> Politicians are supporting more arts and scenes. They want to create buzz.

4. What I Want to Measure (For Both Bars and Cafes)
	* This is going to based on what the quotes say and what I think might help. 

    -	Conservatism vs liberalism
    -	Democratic vs Republican
    -	Rural vs Urban
    -	Political agendas (feminism, egalitarianism, peace, gay rights)
    -	Social cleavages (age, race, gender, religion, class) 
    -	The sense of scene (people’s identifications with a particular place, or multiple places)
    -	“Buzz”

5. How I Am Going to Measure It
	* Below, I will indicate the data available on Yelp, and possible ways of using them.

  * Explicit Political Comments:

	  * Explicit political comments are very rare, but that does not mean that they do not exist. I would need to find some before I decide how to analyze it. Still thinking about this.

  * The way people write:

	  * It is possible to draw a connection between how reviewers structure their reviews and the type of person they are. And we can look at the connection between the types of people who reviewed and the businesses they review in. For example, maybe a certain cafe have reviewers who sound more educated than the reviewers in other cafes. And we can draw connections between cafes and politics. There are many ways to figure out attributes about people based on what they say. For example, look at how often they refer to themselves in the first person singular (using I), first-person plural (we), or third person. People who use “I” are more self-centered and individualistic. Reviewers who use “we” imply that they are visiting a bar with friends. We can also look at how educated a person sounds. Some people use very technical, possibly pretentious, words to describe their meal, while others use slang. Others are very careful about their punctuation and grammar while others aren’t.
	  * Or we can directly relate the words that users use to the business itself.  For example, look at punctuation, especially (!). (!) hints at excitement, passion. Other ways reviewers display their feelings about a business is through the use of ALL CAPS.

  * Connection Between Business Information and the Cafe’s culture:

    * Look at the price range, hours opened, days opened, and specific business information. Price range can indicate class demographics. Hours opened can indicate age demographics (businesses that stay open late until at night are geared more for younger people) and culture (night life culture). 

| More Business Information Labels (note that this is not comprehensive)      |           What this Can Indicate   |  
|---------------------------------------------------------------------------- | ------------------------------  |
| Takes Reservations
| Accepts Credit Cards
| Accepts Apple Pay
| Parking
| Bike Parking
| Good for Groups      | Social gatherings for people to discuss ideas
| Noise Level
| Alcohol
| Outdoor Seating
| Has TV
| Take-out
| Attire                | More formal attire can indicate that a certain place is for those with higher classes
| Good for Kids
| Ambience
| Wi-Fi               | More millenials
| Good for Working

6. Special Features of Yelp:
  *  There are features that users can use (but are optional). This includes the number of check-ins (number of times that Yelp reviewer says to have visited the business) and the number of people who voted for a specific review (users can vote useful, funny, or cool). Possibly, reviews with more votes should be weighted more because more people agree with that review. We can also think about why a certain person would check in multiple times.
  * Note that some reviews are [filtered](https://www.youtube.com/watch?time_continue=71&v=PniMEnM89iY) by Yelp. Basically, only ¼ of the reviews are not recommended (this does not mean one can not see the reviews, it is just not in plain sight). The reviews are filtered by Yelp’s algorithms, and their intent is to filter fake reviews, rants, and unknown people without credibility. The reviews that are filtered do not affect review count or the average stars of a business. The algorithm is also constantly running, so a review that has been filtered can be unfiltered, and visa versa.
  * It is possible to comment on a Yelp review. Many business owners do this to address issues that reviewers have with a business (many times, the business owner apologizes and promises better service). 

7. Who is reviewing:
  * We can look at information relating to who is reviewing. Many of the people who review in cafes and bars have a lot of friends in Yelp (over 100) and have reviewed other things. For example, look at [Christopher V.](https://www.yelp.com/user_details?userid=hT2Mw5m_SXBDVBuvA3KY-w) , who I found since he reviewed [Plein Air Cafe & Eatery](https://www.yelp.com/biz/plein-air-cafe-and-eatery-chicago-2?osq=cafe), a cafe in zip code 60637. Looking at his profile, he seems to love reviewing bars, cafes, restaurants. These reviewers can be a great asset for deciding how to connect different businesses.

	* Some reviewers take pictures of things other than food (like a painting on the wall). Other reviewers also comment about things other than food (like how a cafe feels like the 80’s.)

8. Cafes vs. Bars

  * Look at the time ranges of reviews. Are there certain time periods where the number of new reviews increases/ decreases? This may correspond to times of major political movements, like an election of a new council or president.
	* Compare words that are tied to emotions.
	* Look into other reasons why people say they attend a bar or cafe other than the food. For example, what do people say about their purpose of being in a bar or cafe? What emotions do they feel (relaxed, at ease, “high”, happy)?
	* What cultures do bars/cafes provide? What do the cafe/bars express in terms of art, music, etc. How does this say anything about politics?
	* Look at the number of new bars/cafes that appear every year. This may indicate something about the new political atmosphere.
	* Are there any indications on political issues (like acceptance of Africans, gays, feminists,)
	* What are cafes and bars surrounded by (what restaurants, other bars, or museums, etc surround this location)?
	* These rhetorical questions will be answered when I can get a larger dataset.

9. Problems That I’ve Encountered or Expect to Encounter

  * How to normalize everything:
	  * Dealing with plurals: (cats vs cat)
	  * Dealing with contractions (I’ve vs I have)
	  * Spelling errors
	  * What information am I losing when normalizing? 

  * How to deal with word groups:
	  * If we only consider words by themselves, “I do not like this place” would be interpreted in the same way as “I like this place.”

  * Embedding

    * Possible Ideas for Analysis
	    * Compare clusters of words to the standard cluster (the one made by google).

# February 11, 2019

1. [Gallery of Pilsen Murals](https://interactive.wttw.com/my-neighborhood/pilsen/murals). Here for reference.

2. Email to Clark and Hyesun:

  >> Just to add on to the conversation:

  >> 1. I realized that the synonym generator program that I created can be very useful in gathering more information from Yelp. For example, if we decide one keyword to look for in Yelp is music, it makes sense to look for all words that are a subset of "music". For example, we want to also pick up words like hip-hop, jazz, blues, pop, etc. But if we count the frequencies of only the word "music", we're missing out on words that basically mean the same thing. I think this synonym generator program that I wrote may increase the accuracy of the frequencies of what we are trying to capture.

  >> 2. I'm not sure if anyone has pointed out, but there's a "more business info" section on the right. For example, check out the Wormhole.  This section can help us differentiate Bohemian from corporate. There are descriptions like: 

  >> Ambience: Hipster, Casual, Trendy
  >> Attire: Casual.

  >> These are the two that I picked out because they're the most likely to say something about Bohemian or corporate culture, but there are much more descriptions that we can use. My only concern is the business information is modifiable by anyone. It may also be difficult to compare different businesses because not every business has the same business label categories. For example, the category ambiance appears in the above Wormhole site, but not in L’Ours Bakery Cafe. 

  >> I think someone mentioned the time of day as a possible indicator of corporatism. I'm personally skeptical about this because I can't seem to find any literature on this on Google Scholar. I also wonder whether which is the cause and which is the effect. Does the cafe choose to be Bohemian then pick the hours opened to attract a certain group of people? Or does the cafe pick a certain time to be opened, thereby attracting Bohemian type people who come in those hours?
  However, it can definitely be a good idea to toy with, and it probably wouldn't be that hard to run correlation tests to see if these variables are even related.

  >> 3. Responding to Hyesun's points:

  This is based on my personal experiences, but many cafes and restaurants have chalkboards outside their business, which really appeal to millennials. I notice that cafes or bars with these quirky yet humorous signs are very appealing to the younger generations (since many of these signs employ humor that only young people would appreciate). 

  >> For more of these kinds of chalkboards, see here. I think these signs really contribute to the vitality of the street, but I can't find any academic literature on this, but I think this idea may be interesting to consider.

  >> I have some other ideas, but they're pretty obvious and since Hyesun's expert in walkability and architecture, I don't think I have anything more insightful to really say about Hyesun's point.

  >> 4. Some more ideas possibly to consider.

  >> Since I lived in New York City and have eaten with friends in what I considered to "hip places", one of the things that I noticed was that in many of these place, they would give a very unique name to the food that they serve. For example, in one of the bubble tea places that I visited, they named a kiwi bubble tea drink "The Hulk", and a passionfruit drink "The Boyfriend". It seems to me that places that are Bohemian try very hard to be creative in everything that they do, even for something simple like naming their food. On the other hand, I see that more corporate cafes, like Starbucks, do not really bother to name their drinks with something special. See here for their coffee menu. Of course, proving this connection to Bohemian culture would probably be very difficult unless we can somehow get access to the menu of food in the Yelp data. We would also need a way to measure "creativity", which would take years of research.

  >> 5. Key Words to look for:

  >> My biggest worry about keyword searching is counting frequencies of words that are used in ways that we don't want to consider. For example, the word "hip" can also mean the body part of a human being, which is not what we want to capture. Of course, in this example, it's very unlikely that hip is used this way in Yelp reviews, but it is definitely something to keep in mind. I know machine learning can be used to differentiate the different definitions of the same word, and then pick out when the word is used in a certain way. 

  * Hyesun

    >> 1. Can you send me some output of synonym generator? Did you run it?  What sample size and where?  Send me if you have any results. 

    >> 2. I agree if we can get the information of those attires and ambience. But I found that only some cafes do have these information. Check out this: https://www.yelp.com/biz/la-colombe-coffee-chicago-2?page_src=related_bizes

    >> Some cafes do, but other cafes do not have information. This will lose many sample size if we just want to look at Chicago. 


    >> 3. Yes- visual signage and chalkboard can help pedestrian interactions on the street. So do Awnings and outdoor seating. Typical ways to capture those features are photograph, videos, or diagram, which are qualitative method. If you are interested, you can check out books of William Whyte, Jan Gehl, Allan Jacobs, and New Urbanists.


    >> 4. Like machine learning to analyze painting, you need some criteria to differentiate creative vs. cliche (or conventional) in the name of cafes. In what degree of words should we consider as conventional name?


    >> 5. That is a big downside of automatic search of words, which also happens in Google too. When I type “plaza” in Google map, it shows me a bunch of results with apartments and hotels that have “plaza” in their name. I agree there needs some human handed filtering process at the end. 

    >> Which tasks are you working on now?
    >> Are you also interested in applying machine learning in architectural features?
    >> Ben just told me he wants to do that, and want to check if you are in it as well.

    * JIN:
    >> 1. Not entirely sure about what you mean by sample size, but here's what I meant by synonym generator. Linked word is the starting word. Under each linked word are the associated synonyms. Problems so far: Not all of the synonyms have the same intended meaning. For example, if the linked word is meeting, one synonym is "intersect". But intersect may not have the same nuance that we are looking for.

    >> 2. When I have analyzed data in the past with missing values, I usually either drop the values or set the missing value to the most frequent observation. Of course, these actions have their own limitations (dropping decreases a lot of information). We could also create a new category called NONE.


    >> 4. I thought about this, but the more I think about it the more problematic it is. The biggest issue is that creativity is different for different people and there's no real empirical way to quantify creativity. Maybe I'll come back to this idea in 20 years.

    >> I think Ben will be talking to you about using machine learning for architecture later this week. I will be supporting him in his projects. 


3. Response to Ian's Log
  >> After reading the last 10 pages of the log, I think it would be a good idea for me to be a contrarian and challenge some of these ideas.

  >> Something else potentially interesting is that there are numerous Youtube channels with “café music.” They stream different “types” of café music- so you can have chill jazz, rainy jazz, books and café, winter café, happy café, etc etc. Some of the channels are “live” meaning that they aren’t on any set repeat and continuously play new stuff. Mostly easy listening type of stuff not top 40 hits or anything. Not sure what to do with this right now but it is something I wanted to put out there. 

  >> This inspired me to actually look into the music playlists. After listening to some of the music, I'm actually starting to wonder whether the type of music played in cafes would be a differentiator of Bohemianism. In my view, a Bohemian cafe would somehow need to be unconventional, but I feel that most cafes would have on relaxing music whether it is Bohemian or corporate. And I think relaxing music is probably the only type of music that cafes would play. But a good counterargument to this is that Bohemian cafes prefer different types of relaxing music.



  >> Alexis and I were talking about music's role in cafes, and we discussed how it may be incredibly difficult to gather data about the music that the cafes play. It is definitely a daunting task to go around every cafe and ask for their music list.

  >> Some other thoughts:

  >> I think it may be interesting to think about how music played in cafe changes (or not) throughout the day. Maybe certain cafes attract "corporate" types of people at a certain time a day and "Bohemian" types of people at other times. If there is a pattern, maybe businesses change their music type to fit the type of people who at that certain time. Maybe during the data collection process, we can ask the business owner why they picked a certain music genre over another.

  >> I skimmed the paper: The_geography_of_music_preferences that was mentioned in Ian's log

  >> sophisticated and contemporary—are associated with more afﬂuent, more educated, more knowledge-based places that are also denser, more diverse, and politically liberal. Two other musical types—unpretentious and intense—are associated with less advantaged, less educated, more working-class places that are more politically conservative and have larger white populations.

  >> Sounds like sophisticated and contemporary can possibly be a good indicator of Bohemianism.

  >> The genre types connected to them are: 
  >> Folk, bluegrass, blues, jazz, opera, classical, world, Rap, soul, funk, reggae.

  >> I question whether most people can even differentiate these types of music. If they can't, I wonder if music could still predict Bohemianism.

# February 14, 2019

1. Email To Hyesun on GIS Graphing

  * HYESUN
  >> I created maps showing distribution of cafes, and changes of cafe vs. bars. 

  >> I also zoomed in NYC, Chicago, LA, and New England region to see local variations.
  >> In all these area, cafes are growing and bars are going down. There are more zip codes where cafes increase and bars decrease than zip codes with bars increasing. Although having increase of cafe and decrease of bars is general trend, we can look at more regional differences. 

  >> In State level,
  >> Cafes 11% increased, Bars 4% decreased in Illinois
  >> Cafes 27% increased, Bars 4% decreased in New York
  >> Cafes 19% increased, Bars 5% increased in California
  >> Cafes 2% decreased, Bars 46% increased in D.C
  >> Cafes 42% increased, Bars 24% increased in Maine - Other New England states also generally showed increase of both cafes and bars!

  >> These aim to help understanding of national distribution. Any other suggestions to see more variations?I can join with demographics or Scenes dimensions? 

  >> I have geocoded cafe and other businesses for Chicago, Paris, and Seoul which I will link with more street level urban forms as case study.

  * JIN

  >> Would it be interesting (or possible) to look at the number of cafes per certain population? So for each region, divide the number of cafes by total population for normalization. I'm only asking this since the first map doesn't tell me much because there may be more cafes simply because there are more people in the area. I feel that the first map is telling me
  more about the population distribution than cafes.

  >> divide the number of cafes in a certain area by the total population of that area.

  >> I also think it may be useful to look at gradients (the percent change of cafes) than binary (whether it either increased or decreased).

  >> These are only suggestions.

  * HYESUN

  >> Thanks for calling out those maps.
  >> I almost forgot about them. 
  >> Yes. I can do “cafes divided by population” and “percentage change”  That’s very handy in GIS. 

  >> Have you seen this? https://www.bustle.com/articles/155686-which-us-city-has-the-most-coffee-shops-these-are-the-best-places-for-coffee-lovers

  >> A table in this page shows the number of cafes per 10,000 people, If I make a map based on that, I believe Seattle, San Francisco, Portland, and D.C, Pittsburg will pop up more. 

  >> This is a general picture of which regions have more coffee industries, but we should also look at street level context and neighborhood. 

2. Email on Mural Data
  * https://www.muralmapla.com/

  * BEN
  >> I am a researcher in Professor Terry Clark's sociology group at the University of Chicago. We are interested in using image processing algorithms to analyze mural art to better understand the relationship between the content of mural art and the communities. 

  >> To do this, we need a data set of murals that also have the specific addresses of the murals attached. The images and addresses used in Mural Map LA would be perfect for this. Do you have this data stored in a way we could download? If so, would you be willing to provide us with it for research purposes? 

  >> Thanks for your time.

  * CHELSEA
  >> Thank you for reaching out! This is an incredible request and I will work hard to ensure you have the information you need to support your work. 

  >> Can you first let me know the timeline you are working on and which data you'd like to see included alongside each photo? I have well over 1500 photos in my collection but not all are publicly available yet. 

  >> Happy to jump on the phone sometime this week to discuss more.

  * BEN
  >> As I mentioned, I have been looking for data sets for mural art that have been geocoded. 

  >> I reached out to the person running the LA database, Mural Maps LA, that Professor Clark mentioned in our last meeting. Here’s her reply. See below

  >> We should discuss this at the meeting tomorrow. 1500 is a decently sized data set as far as images go so I think this is a worthwhile opportunity to at least get data. 

3. Ying Cai's Thesis Proposal

  * YING CAI
    >> My name is Ying Cai, a master student. Thanks for your letting me participate in the scene research meeting last time. After last scene research meeting, I have shifted my research object from restaurant to meetups that happen at a rather fixed place, like book club, business forum, drawing session and so on but still based on the scene theory. The attached are my new proposal and a sample of the events data (since the whole dataset is too large). If you might be interested in this research theme, may I have a further discussion with you?

  * TNC
  >> This looks terrific! 

  >> Tell us a little more about the source and how /why choose these specific organizations?  What is in and what is out and why? Is it consistent across locations?

  >> How build a model for other variables? Rough draft available?

  >> Happy to Skype in next days. Send email to others too please?

  * JIN
  >> I'm confused about how the master proposal would be useful for me. I get that I would probably be applying a similar sort of geographically weighted regression, but I'm not sure how else I can use this proposal since it lacks a lot of details. Am I missing something?

  * TNC
  >> By master proposal do you mean the rough draft proposal for an MA by. Yong Cai?  

  >> At this point is there it is a rough draft in the question is how might we potentially overlap help make suggestions or whatever. One of the main themes that we have discussed is what are the types of neighborhoods and characteristics such as are included in the murals the Facebook for your discussions of cafés in bars and other institutions in different neighborhoods. How in one of the pieces fit together? How can we use statistical procedures it will identifyTiny pieces Atoms and put the Atoms together and more meaningful larger sections to build  people and animals to follow the analogy.

  >> These data could provide one more set of variables in addition to the amenities and other things which we have.

  * JIN

  >> I took a look at this dataset, and it is quite interesting.
  >> This site here contains graphs that showcase the information. 

  >> The most prominent variables for me were:

  >> description (describes what the event is about).

  >> There was so much diversity in the descriptions that it may be hard to extract valuable insights. But we can probably try to search for keywords just like in Yelp. We could even run the same keywords that we created for Yelp. 

  >> duration (how long the meeting last)
  >> There are probably correlations between how active a scene is and how long a meeting is in that scene.

  >> category name (example: career and business, book clubs, art and culture)
  >> I thought that these categories were incredibly broad, and not all were related to scenes (like career and business, which was a very prominent category in these meetings).

  >> Since the data is geolocated by longitude and latitude, we create a similar map to what Hyesun created for displaying the increases/decreases in the number of cafes. Ying Cai graphed the categories on a map, which was very interesting. But we can extend this further: we can create a graph for increases/decrease of a particular category over a certain period of time.

  >> I do have some reservations about using this data:

  >> My biggest problem is that these meetings are quite temporary compared to the things that we are studying. Cafes and murals last, and we can argue that what stays create scenes; events that only happen once are too transient to develop a scene.

  >> Also, judging from the data, a lot of the reasons for meetings do not create what we defined as a scene. For example, meeting for jobs and businesses and book clubs.

  >> Just some preliminary thoughts.

4. Email on Trump Paper R Error
  * JIN:
    >> You said there was an error in the trump R code?

    >> I presume it's this file or this one.

    >> If there's a problem, could you state the problem so I could try to help?

    >> I'm not incredibly familiar with R, but I can try.

  * HYESUN
    >> Are you joining Liang Cai on Trump project now on?
    >> The problem came from more complexity of reasons, not just R code. It’s combination of problem of data file itself and missing counties coming from merging process. If you are on this project, I think you should read Liang Cai’s log as well as my log on Trump. Check both Trump 2 and 3 folder. These summarize the problems, and Liang is trying to resolve the issue. Liang is the person who has the most up-to-date version of log on Trump data analysis. Have you communicated with him? I am cc-ing him here so you guys can share thoughts.

5. Dataset Collection.
  * See [here](https://github.com/JinLi711/UIA/blob/master/Data/dataset_links.md) for what I compiled

# February 17, 2019

1. Had to deal with the gitignore file.

2. I think it would be a good idea to leverage Google Cloud's Natural Language API.
  * [GCP Natural Language](https://cloud.google.com/natural-language/)
  * [GCP Natural Language Basics](https://cloud.google.com/natural-language/docs/basics)
  * [GCP Natural Language Docs](https://cloud.google.com/natural-language/docs/)
  * it essentially performs machine learning text analysis using Google's algorithms.
  * the problems I see with this:
    * black box model. No clue why the model churned out this certain output.
  * But anyways, here's some research on what GCP NLP can do.
    * sentimental analysis: predict whether a text is positive, negative, or neutral.
      * Not incredibly useful for us because we aren't focused so much on what the person is feeling as we are with the culture of the person. However, I imagine that in a review, the attributes that define bohemianism may correlate with the sentiment, since I noticed that when a person is satisfied with the cafe that they ate in, they tend to describe other attributes that contribute to their positive review (like the vibe of the atmosphere). Also, the number of stars that a person rates already display a sentiment.
    * Entity analysis
      * finds the proper and common nouns (like public figures, landmarks) from a text and returns information about them
      * can also return how the writer feels about the entity.
      * This is probably the most useful because it can directly link to things that we would want to analyze. For example, if a person in Yelp review mentions a music artist name, we could actually find out information about that artist and more importantly detect that the music artist is actually there. The same can be said for other pronouns like murals or street names. For example, if the person mentions Back Street Boys, using our old text analysis methods, we would have never picked up that the person is talking about a music artist.
      * This solves indirect references.
    * Content Classification
      * analyzes text content and returns content category. I don't feel that this can be incredibly useful because I feel that the content returned will almost always be related to food, which is not what we are searching for in Yelp.
  * [Here's](https://cloud.google.com/natural-language/pricing) the pricing if we were to be interested in using this.
  * [Google Cloud AutoML Natural Language](https://cloud.google.com/natural-language/automl/docs/). This is used to train your own model. Requires the labels. If we ever use this, we would probably have the categories Bohemian, corporate, and neighborly as labels. However, I am strongly against using this because I highly doubt that this would provide meaningful results, especially when the lines between the categories are quite subjective.

3. Email To Hyesun

  * JIN:
    >> I am currently working on normalizing text in Yelp. I think I will create a report on it soon just describing the process of normalizing text. 

    >> What I mean by normalizing text is changing the words so we can analyze it will higher accuracy. For example, if I were to look for frequencies of the word "apple", I wouldn't want to miss "apples". There are a variety of normalizing steps that I will describe.

    >> I've been looking at Google Cloud Platform Natural Language. One of the amazing things that it could do is analyze text and find proper nouns. For example, if a reviewer mentions "Back Street Boys", Google Cloud can detect it. This could be very useful for music analysis, especially when reviewers mention more specific music that we want to capture. In addition, Google Cloud can perform sentiment analysis on these extracted pronouns (finds out how the reviewer feels about "Back Street Boys".

    >> The only qualm I really have with Google Cloud text analysis is that its a black box: it would be very hard to tell why we received a certain output.

    >> Thoughts on Google Cloud usage?

  * HYESUN
    >> 1. Keywords on Yelp

    >> So does it update what you did on finding synonyms?
    Normalizing & Google Clouds sound fine. You showed me example of synonyms last time, but I don’t think I have seen any output yet. The early output of keywords correlation did not show any significant difference between cultural types because most of reviews are centered on Food, not other things like music.

    >> Have you actually applied using synonyms in trying extracting words in cafes for the same sample size? I think that should be the first output to share with me and others, then you can continue exploring other options like normalizing, Google Clouds, etc. But as I mentioned there is a fundamental constraint of Yelp in itself as a platform for review on food mostly, unlike other social media allowing hashtag or more various user expressions. 

    >> 2. Machine Learning 

    >> One thing I also want to suggest is that you and Ben can possibly apply machine learning in analyzing those photos on Yelp or other social media. Painting or murals might be more complicated to do with machine learning because there is usually certain way of intention that artists want to express their thought. So, in that sense, there is already category of what elements are categorized as Baroque, Rococo, Modern, etc as they are displayed in the museum. What seems more interesting from social science perspective is how people actually respond to those paintings, such as people would go to places, like cafes and bars near murals more frequently, or people participate in group activities in that neighborhood more, etc as a measure of buzz.  

    >> I think that’s why applying machine learning in those reviewers’s photographs might be more feasible and easier, because photographs are more neutral than paintings in terms of style. We can perhaps use machine learning for differentiating those photos centered on food / activities / atmosphere which might be easier than analyzing paintings. Using machine learning in analyzing architectural form is same logic. There are many things that define architectural form, such as height, material, color, transparency, setback, etc. Since we can’t analyze every aspect through machine, you should start with simple thing in a hierarchy as a first step. 

    >> These should be based on understanding of basic/simple method from past literature. Have you figured out how to do so yet? Just trying to help and think about ways for something simpler. 

    >> What do you think?

  * JIN

    >> 1. Here are the frequencies of keyword synonyms (not including the keyword themselves). I made the plot so that it would not plot frequencies of words that are less than 10. 

    >> The graph names correspond to the category of cafe, and the businesses were from Alexis's list a while back.
 
    >> The graph doesn't say anything meaningful yet because most of the words that show up are loosely synonymous to the starting keywords.

    >> 2. I think it is a very good idea to try to analyze Yelp /Instagram photos. I just want to build off of the email the other day, where you said the arrangement of chairs can impact the quality of scenes.

    >> So Google Cloud has this service (costs money) where they can label the content (and location) of items in a photo. For example, if we have this picture:

    >> Google cloud is able to draw a box around each chair/ table. If we have a picture of a plate of food, Google Cloud is able to draw a box around each item of food. This can help differentiate between food /activities/atmosphere of images.

    >> However, Google Cloud can only detect the content of the images; it cannot detect something less concrete like a style of the architecture. 

    >> Me and Ben are still discussing the machine learning project.

    >> 3. I will continue to think through the normalization step, which is going to be hard because the English language is incredibly complicated.

# February 18, 2019

1. Read up on [this Stanford lecture notes](https://web.stanford.edu/~jurafsky/slp3/2.pdf) for help on text normalization. 

2. Also looked into this [wolfram site](https://reference.wolfram.com/language/guide/TextNormalization.html) for text normalization.

3. Also spent a lot of time searching for google results on ideas for text normalization. Nothing else valuable showed up.
    * Google Search Term: text normalization

4. Converting markdown to documents.
  * pandoc -o Log.docx -f markdown -t docx Log.md

5. Here's my write up for text normalization.
  * [Github Link](https://github.com/JinLi711/UIA/blob/master/Yelp/NLP%20for%20Yelp/normalizing_text.md)

# February 20, 2019

1. Google Maps API:
  * [Routes:](https://cloud.google.com/maps-platform/routes/) data on roads and real time traffic
  * [Places:](https://cloud.google.com/maps-platform/places/) gives information on the businesses
  * [Maps:](https://cloud.google.com/maps-platform/maps/) gives information on the maps

2. Goal: Open up the spss merge file and think about how I can correlate the existing data with the Yelp data. Look at the differences on a map, and understand why there are these differences. Ask the library to help me download SPSS.

# February 21, 2019

1. Downloaded US_merge_hyesun_final.sav from OneDrive. Planning to use this file to do correlation analysis. But first, I have to understand this file first.
  * Looked into the columns using R. Columns are very uninformative, need to find a file in OneDrive to find description of column names. Couldn't find it, so I asked Hyesun if she knew where it is.
  * EDIT* Turns out the descriptions are already included in the merge file.
  * Note that all the columns are opened up as strings, meaning I have to convert strings into numbers when neccesary.
  * Would it be valuable to look into every single variable and predict whether the variable has any indication of appearances of words?
    * OH NAH.
    * BUT I will skim the variables to see what sticks out to me through intuition. Also, it's incredibly hard to do copy and paste in R, so I'm just going to put keywords here to search. 
    * Also, there are some variable descriptions that I do not understand, so I will just ignore those.
    * Why are there duplicate column names? Or are they really duplicates? I can check, but this is distracting. Will do this later.


    | Variable      | Description |
    | ------------- |-------------|
    | zipcode       |             |
    | NAICS         | 15 scenes variables. Note that there are different variations of this. |
    | STUSAB        | state |
    |               | population |
    |               | latitude  |
    |               | longitude |
    |Age            | Age groups. Search 'years'|
    |               | Races. Note that this will be hard to search. Might have to just scroll through until I see this. |
    |               | DDB. Can also search 'performance' |
    |               | bizzip  |
    |               | patents  |
    |               | income  |


2. Some merging variable ideas:
  * Each keyword can be a variable, and values would be its appearance in each zipcode.

3. Did some more research on Geographical weighted regression.
  * [Overview](https://www.mailman.columbia.edu/research/population-health-methods/geographically-weighted-regression)
  * Like OLS, but allows independent and dependent variables to vary by locality.
  * construct a OLS for each location in the dataset.
  * Should I even bother learning about implementing this in R? I can't do this in python since opening SPSS files in Python is just awful. I tried downloading SPSS to csv and opening in Python, results were all messed up. I'm not too good with R, so the learning curve may not be worth it. It would probably just be a lot easier for me to merge results, then give the results to Hyesun (or anyone else) to run in ARCGIS.

4. So in terms of correlations:
  * here's a great [link](https://www.dummies.com/programming/r/how-to-deal-with-missing-data-values-in-r/) about correlations in R with missing values.
    * Basically, will return NaN if any values are NaN.
    * But we can switch its functionality so it just will not consider NaN values.

5. So since I'm doing computations in Python / C, I need to find a way to take the outputs of these calculations, and open it in R. Then I need to find a way place whatever is neccesary into a SPSS file.
  * Added more to my plan page [here](https://github.com/JinLi711/UIA/blob/master/Yelp/NLP%20for%20Yelp/analysis_plan.md)
  * Read this [article](https://www.searchtechnologies.com/blog/natural-language-processing-techniques) to help me add to the plan.
  * Google Search: text mining. Here's a [wiki](https://en.wikipedia.org/wiki/Text_mining) for getting started.

# February 22, 2019

1. Email on Great Names Department
  * HYESUN
    >> There is also this name, “Department of Coffee and Social Affairs” I recently visited. There are two locations, and one of them is in downtown, next to Federal Reserve Bank and few other government buildings, which got me instantly think their name in the signage was one of government buildings too. I realized they were cafe when I went inside. Their first location in Lakeview is very different from this downtown location, more like a typical small independent cafe.
  * TNC
    >> Wonderful PHOTO!
    >> What is this like in Seoul? Shanghai? Paris?  Do we have any info from Chicago now, Heysun?
    >> Might  Carolyn serach for these  comparative photos? and Maybe data sources for numbers over time, by neighborhood,  or text about their goals etc? 
  * Not sure how this is relevant to me.

2. Added on to the plan page [here](https://github.com/JinLi711/UIA/blob/master/Yelp/NLP%20for%20Yelp/analysis_plan.md). Here's the plan for reference:


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
    ```
        {
            "really": 2,
            "apple": 1
        }
    ```

4. Write another algorithm that outputs word counts for all possible words. Note that I do not do this before the regular search because this will not allow me to search for phrases that are seperated by spaces.
    * Example: "I really really love apple."
    * Output:
    ```
        {
            "i": 1,
            "really": 2,
            "love": 1,
            "apple": 1
        }
    ```

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
    * I might also split json files by zipcode, but also maybe not.

Example of first file:

```
{
    "BUSINESS1": 
                {
            "really": 2,
            "apple": 1
                }, 
    "BUSINESS2": 
                {
            "really": 5,
            "apple": 4
                },
}
```

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

* I need to write something that allows others to be able to visualize what's inside these files.

* Searching may take forever in Python. I will write this code in C, but analyze the results in Python.
    * If I write the code in C, here would be the steps: 
        1. Open up the file as a string.
        2. Search for number of appearances in the string.
        3. Write to a json file a dictionary mapping a searched term to its frequency.
        4. Open the json file into Python for analysis.




# Data Structures

## Text normalization

This will be done in Python:

Need to think about this after I get the file.

## Word Search

This will be done in C:

For a single business, it's going to be a basic struc, with all the neccessary fields.

```
typedef struct _business_info{
    char * all_reviews;
    unsigned int zipcode;
    etc...
} business_info
```

For all the businesses together, it is going to be an array

```
business_info * all_businesses[];
```





# Find Correlations

## Geographical Weighted Regression

For each variable of interest from the merge file, correlate it with the data from the json file.






# Inserting Data

So by the end, we will have a file (probably a json file) that maps each business to its information. 

We can do another level of aggregation to combine businesses together to the zip code level.





# March 1, 2019

1. So one of my current goals for this week is to search for possible keywords that may be interesting to consider and search for in Yelp. 

This is given to me by Hyesun:

Supposedly Bohemian words:

*Food words:* espresso, coffee, latte, pastry, bakery, 

*Event words:* entertainment, festival

*Imagery words:* decoration, style, street, graffiti, painting, art, mural, gallery, tattoo

*Feeling words:* music, vibe, hip, unique, comic, 

*Social problem words:* LGBT, social, justice, sustainability

*People words:* barista, friend, artist, writer, entrepreneur
studio, walk, bicycle, walk, bicycle



Corporate / utilitarian:

*Food words:* espresso, coffee, latte, pastry, bakery, 

*Moving words:* workout, commute, walk, subway, transit, bus, fitness, quick

*Working words:* work, studying, co-working, meeting, office, laptop, WiFi, colleague

*Place words:* museum, apartment, CBD, downtown, tourist

*Others?* take-out outlets


Traditional, neightborly, local:

*Food words:* espresso, coffee, latte, pastry, bakery, 

*People words* kids, children, friend, family, neighborhood, community, hang

*Places* landmark, school, church, flea market, townhouse, farmer market, park

*Adjectives* local, family-owned, housemade, traditional, famous, cozy

*Others?* history, grocery, sofa, dog, walk

Some of these words are questionable, and I wonder why I was sent some of these words. For example, what does coffee have anything to do with the scenes variables? But anyways, here are the starting words, and I have to search for more words that can possibly correlate the scenes variables.

So I'm just going to go down through the 15 scenes variables and do some word association to see if I can come up with any words.

















