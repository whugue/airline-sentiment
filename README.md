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


### Repo Contents
#### A) Home folder : 
Python Scripts and Notebooks :

1. **TextBlob-Sentiment-Analysis.ipynb**: Unsupervised sentiment analysis of 1,000 tweets to United Airlines using the TextBlob polarity analyzer

2. **AddSentiment.py**: Add TextBlob and VADER sentiment polarity scores (ranging from -1.0 for very negative to 1.0 for very positive) to CrowdFlower data

3. **Airline-Sentiment.ipynb**: Compare performance of unsupervised (TextBlob, VADER) and supervised (Naive Bayes, SVM) sentiment classifiers on a test 
set extracted from the CrowdFlower data.


#### B) data/crowdflower :
Source and Derived Data used in analysis:

1. **Airline-Sentiment-2-w-AA.csv**: Corpus of ~15,000 tweets from February 2015 directed to U.S.-based airlines. Each tweet was labeled as positive or negative in sentiment by CrowdFlower's contributors. 

2. **airline_sentiment_with_tb_vader.pkl**: Pandas dataframe containing all tweets in the **Airline-Sentiment-2-w-AA.csv** datafile, with TextBlob and Sentiment polarity scores matched to tweets. Output of **AddSentiment.py** data.

Note that NLTK's twitter samples and tweets from the Twitter API are also used in analysis, but are not saved to this repo.


#### C) graphics/ :
JPG/ PNG files containing graphics used in analysis.


#### D) deck/ :
Final PowerPoint Deck for Metis presentation given at Metis on 5/31/2016






