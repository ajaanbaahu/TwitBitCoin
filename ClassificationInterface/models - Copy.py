from mongoengine import *
import datetime
connect("SentimentDB")

class Tweet(Document):
	tweet=StringField(max_length=255,required=True)
	user=StringField(max_length=255,required=True)
	tweet_date=DateTimeField(required=True)
	tag=StringField(required=True)
	user_type=BooleanField(required=False)
	

test_tweet=Tweet(tweet="This is test tweet", user="Test_User",tweet_date=datetime.datetime.now(),tag="Positive",user_type=True).save()


## this is test


