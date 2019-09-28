#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import json
import tweepy
from tweepy import OAuthHandler, Stream
import re
from tweepy.streaming import StreamListener
from datetime import datetime, timedelta
consumer_key = "xxx"
consumer_secret = "xxx"
access_key = "xxx"
access_secret = "xxx"

def get_all_tweets():
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = '@museumofscience',count=25)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    #oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = '@museumofscience',count=25)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
       # oldest = alltweets[-1].id - 1
        if(len(alltweets) > 25):
             break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
    return alltweets   

def get_score(text):
# Imports the Google Cloud client library
	from google.cloud import language
	from google.cloud.language import enums
	from google.cloud.language import types
	import testjson
# Instantiates a client
	client = language.LanguageServiceClient()

	sentimentsList = []

#num_texts = 0 #hold number of texts considered (also iterator for while loop)

# The text to analyze

	text1 = testjson.gettext()
	for text1 in text:
    #num_texts = num_texts + 1
    #text = u"This is BIZARRE! Here's Joe Biden telling the story of his face-off with a gang of razor-wielding ne'er-do-wells led by a guy named 'Corn Pop.'"
            document = types.Document(
                content=text1,
                type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
            sentimentsList.append(client.analyze_sentiment(document=document).document_sentiment)
            avg_sentiment = (sum(sentimentsList))/(len(sentimentsList))

	#return avg_sentiment

    #print('Text: {}'.format(text1))
    #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
                         
#print('The average sentiment is %d', avg_sentiment)
    #write tweet objects to JSON
	file = open('tweet1.json', 'w') 
	print ("Writing tweet objects to JSON please wait...")
	for status in alltweets:
            json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
	print ("Done")
	file.close()
   
    #pass in the username of the account you want to download
	get_all_tweets('@museumofscience')

	return avg_sentiment

import json
import demjson
import re
def gettext():
  with open("/home/ece-student/tweet.json", encoding='utf-8') as f:
    line=f.read()
    line=re.sub("'","\"",line)
    line=re.sub("u'","\"",line)
    d = json.loads(line)
    text = d["text"]   
    return text
    f.close()

def main():
    collectTweets = get_all_tweets()
    avg_sentiment, sentimentsList=get_score(collectTweets)
           
    print("The average sentiment is: ", avg_sentiment)
                         
#print (gettext())
if __name__ == '__main__':
    main()

# We used Amanda Maasa's github to help get us over our final issues with the code.
