import datetime
import tweepy
from flask import url_for
from mongoengine import *
connect("SentimentDB2")

class Tweet(Document):
    tweet=StringField(max_length=255,required=True)
    #user=StringField(max_length=255,required=True)
    #tweet_date=DateTimeField(required=True)
    #tag=StringField(required=True)
    #user_type=BooleanField(required=False)


#test_tweet=Tweet(tweet="This is test tweet", user="Test_User",tweet_date=datetime.datetime.now(),tag="Positive",user_type=True).save()
#test_tweet2=Tweet(tweet="This is test2 tweet", user="Test_User2",tweet_date=datetime.datetime.now(),tag="Negative",user_type=True).save()

ckey=''
csecret=''
atoken=''
asecret=''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

public_tweets = api.search('bitcoin')
user = { 'nickname': 'Ryan' } #fake user
for thing in public_tweets:
	Tweet(tweet=thing.text).save()
#twwet=Tweet(tweet=public_tweets.text).save()


