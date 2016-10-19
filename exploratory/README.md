### Metis Project 4: Rule-Base vs. ML-Trained Sentiment Analysis
How does the performance of various supervised ML and rule-based methods compare when tasked with identifying sentiment in Tweets to U.S. airlines?

Read my [blog post](http://www.huguedata.com/2016/07/10/frustrating-skies/) for a full discussion, or check out the [slides](https://github.com/whugue/airline-sentiment/blob/master/exploratory/deck/airline%20sentiment%20presentation.pdf) from my Metis presentation.


### Program Flow
The table below provides high-level overviews of what each analysis script does. More information (including specific input/ouput data) can be found in each script's header.


Program 	| Description | 
----------- | ----------- |
01-Apply-Sentiment.py | Add rule-based TextBlob and VADER sentiment polarity scores to CrowdFlower data.

02-Text-Blob-Sentiment-Analysis.ipynb| Sentiment analysis of 1,000 tweets to United Airlines using TextBlob.

03-Airline-Sentiment-Analysis.ipynb | Compare performance of rule-based and supervised ML-based sentiment classifiers.


### Code Dependencies
Before running any of these scripts, please make sure to have downloaded: 

NumPy, Pandas, Sci-Kit Learn, Matplotlib, Seaborn, Pylab, re, NLTK (including their twitter samples corpus), TextBlob, vaderSentiment, Pickle, Cnfg, Os, TweePy (Twitter API Python Wrapper), MongoDB and PyMongo






