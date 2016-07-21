### Metis Project 4: Airline Sentiment Analysis

How does the performance of various supervised and unsupervised machine learning methods compare when tasked with identifying negative, complaint-ridden tweets sent to U.S. airlines?

Read my [blog post](http://www.huguedata.com/2016/07/10/frustrating-skies/) for a full discussion.


### Code Dependencies
* Numpy
* Pandas
* Sklearn
* Matplotlib
* Seaborn
* Pylab
* re
* NLTK (with NLTK twitter samples corpus)
* TextBlob
* vaderSentiment
* Pickle
* Cnfg
* Os
* Tweepy
* MongoDB and PyMongo


### Data
There were three sources of data used in this analysis:
1. *NLTK Tweet Data*: General twitter samples provided by NLTK, labeled by sentiment (either positive or negative) (not saved to this repo, but available from NLTK).
2. *CrowdFlower Tweet Data*: A corpus of tweets to U.S. airlines, scraped from twitter and labeled by sentiment by CrowdFlower contributors (saved here: *data/crowdflower/Airline-Sentiment-2-w-AA.csv*)
3. *Twitter API Data*: A stream of 1,000 tweets to United Airlines sourced from the Twitter API (not saved to this repo).


###Python Scripts, IPython Notebooks, and Program Flow:
1. *TextBlob-Sentiment-Analysis.ipynb*: Unsupervised sentiment analysis of 1,000 tweets to United Airlines using the TextBlob polarity analyzer.
2. *AddSentiment.py*: Add TextBlob and VADER sentiment polarity scores (ranging from -1.0 for very negative to 1.0 for very positive) to CrowdFlower data.
3. *Airline-Sentiment.ipynb*: Compare performance of unsupervised (TextBlob, VADER) and supervised (Naive Bayes, SVM) sentiment classifiers on a test 
set extracted from the CrowdFlower data.

###Other Fun Stuff:
1. *graphics/*: JPG/ PNG of Matplotlib and Seaborn graphics produced for my final presentation and blog post.
2. *deck/*: Final powerpoint deck associated with the presentation I gave at Metis on 5/31/2016.






