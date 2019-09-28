#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import json

consumer_key = "xxx"
consumer_secret = "xxx"
access_key = "xxx"
access_secret = "xxx"

def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('tweet1.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ("Done")
    file.close()

if __name__ == '__main__':
   
    #pass in the username of the account you want to download
    get_all_tweets('@museumofscience')
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import testjson
# Instantiates a client
client = language.LanguageServiceClient()

avg_sentiment = 0 #hold average value of text sentiments
num_texts = 0 #hold number of texts considered (also iterator for while loop)

# The text to analyze

while num_texts < 25:# can also ask user for num of texts to analyze, though would need add'l variable
    text1 = testjson.gettext()
    num_texts = num_texts + 1
    #text = u"This is BIZARRE! Here's Joe Biden telling the story of his face-off with a gang of razor-wielding ne'er-do-wells led by a guy named 'Corn Pop.'"
    document = types.Document(
        content=text1,
        type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    avg_sentiment = (av_sentiment + sentiment) / num_texts

    print('Text: {}'.format(text1))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

print('The average sentiment is %d', avg_sentiment)
