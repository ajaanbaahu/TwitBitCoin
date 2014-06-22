from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='6el3wZb5jPjhwBgnYAIga4unx'
csecret='rgE1HmzUYNGP9F2M5x14c1CYM57FBax7o3IxbELdPvwwiUYKiW'
atoken='2576316331-X8N9hfQdRAEURQr8KWeY8iADs7dppE9YNOLiECy'
asecret='sVZym9N0JdnH8IXjbgvWTjMJHNIgyFNrqXBlvJx5tRgFj'

class listener(StreamListener):
	def on_data(self,data):
		print data
		return True
		
	def on_error(self, status):
		print status
		
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["car"])