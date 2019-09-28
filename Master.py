#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import json
import json
import demjson
import re


#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = '' 


def get_all_tweets():
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = "ussconstitution",count=10)
    for tweet in new_tweets:
        alltweets = alltweets + [tweet.text]
    return alltweets
tweet1=get_all_tweets()
print(tweet1)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
sentiment_score_list = []
def get_score(text1):
    for tweet in text1:
        client = language.LanguageServiceClient()  
        # The text to analyze
        document = types.Document(
            content=tweet,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment_score_list.append(client.analyze_sentiment(document=document).document_sentiment.score)

    average_sentiment = sum(sentiment_score_list)/len(sentiment_score_list)
    return average_sentiment
print(get_score(tweet1))

def main():
    collectTweets = get_all_tweets()
    avg_sentiment, sentimentsList=get_score(collectTweets)
           
    print("The average sentiment is: ", avg_sentiment)
                         
#print (gettext())
if __name__ == '__main__':
    main()

# We used Amanda Maasa's github to help get us over our final issues with the code.
