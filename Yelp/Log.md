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



