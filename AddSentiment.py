import numpy as np
import pandas as pd
import pickle

from textblob import TextBlob
from vaderSentiment import vaderSentiment as vader

#Read-In Aggregated Crowdflower Data
variables = ["_unit_id","_trusted_judgments","airline_sentiment","airline_sentiment:confidence","airline","text"]
cf = pd.read_csv("data/crowdflower/Airline-Sentiment-2-w-AA.csv")[variables]


#Create Binary Classifier
cf["sentiment"] = np.nan
cf.ix[cf.airline_sentiment=="negative", "sentiment"] = 1
cf.ix[cf.airline_sentiment.isin(["neutral", "positive"]), "sentiment"] = 0
cf.drop("airline_sentiment", axis=1, inplace=True)


#Apply TextBlob and VADER Sentiment 
def text_blob_sentiment(text):
    text = text.decode("ascii", errors="ignore")    
    return TextBlob(text).sentiment.polarity

def vader_sentiment(text):
	text = text.decode("ascii", errors="ignore")
	return vader.sentiment(text)["compound"]

cf["text_blob_sentiment"] = cf.text.apply(text_blob_sentiment)
cf["vader_sentiment"] = cf.text.apply(vader_sentiment)

##Output to Pickle
cf.to_pickle("data/crowdflower/airline_sentiment_with_tb_vader.pkl")