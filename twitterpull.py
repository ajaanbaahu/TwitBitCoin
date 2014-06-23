from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, json

ckey='6el3wZb5jPjhwBgnYAIga4unx'
csecret='rgE1HmzUYNGP9F2M5x14c1CYM57FBax7o3IxbELdPvwwiUYKiW'
atoken='2576316331-X8N9hfQdRAEURQr8KWeY8iADs7dppE9YNOLiECy'
asecret='sVZym9N0JdnH8IXjbgvWTjMJHNIgyFNrqXBlvJx5tRgFj'

class listener(StreamListener):
	def on_data(self,data):
		try:
			tweets= json.loads(data)
			print type(tweets)
			#ids = [tweet['id_str'] for tweet in tweets]
			#saveFile=open('twitDB.csv','a')
			#saveFile.write(tweet)
			#saveFile.write('\n')
			#saveFile.close()
			#print tweet
			return True
		except BaseException, e:
			print 'failed on data', str(e)
			time.sleep(5)
	
		
	def on_error(self, status):
		print status
		
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["car"])