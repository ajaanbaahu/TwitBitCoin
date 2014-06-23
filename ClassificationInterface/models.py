import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from mongoengine import *
import datetime
connect("SentimentDB")

ckey='6el3wZb5jPjhwBgnYAIga4unx'
csecret='rgE1HmzUYNGP9F2M5x14c1CYM57FBax7o3IxbELdPvwwiUYKiW'
atoken='2576316331-X8N9hfQdRAEURQr8KWeY8iADs7dppE9YNOLiECy'
asecret='sVZym9N0JdnH8IXjbgvWTjMJHNIgyFNrqXBlvJx5tRgFj'


class Tweet(Document):

    tweet=StringField(max_length=255,required=True)
    user=StringField(max_length=255,required=True)
    tweet_date=DateTimeField(required=True)
    tag=StringField(required=True)
    user_type=BooleanField(required=False)

class listener(StreamListener):
    def on_data(self,data):
        tweet= json.loads(data)
        try:
            text=tweet['text']
            user=tweet['user']
            tweet_date=tweet['time']
            tag=[]
            user_type=[]
        except:
            pass
        return True
        return text,user,tweet_date,tag,user_type
    def on_error(self, status):
        print status


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["car"])

test_tweet=Tweet(tweet="This is test tweet", user="Test_User",tweet_date=datetime.datetime.now(),tag="Positive",user_type=True).save()
test_tweet=Tweet(listener.on_data())

