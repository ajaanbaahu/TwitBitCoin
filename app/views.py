from flask import render_template
from app import app
import tweepy
from mongoengine import *
import datetime
from models import Tweet
connect("SentimentDB1")

@app.route('/')
@app.route('/index')
def index():
	ckey=''
	csecret=''
	atoken=''
	asecret=''

	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	api = tweepy.API(auth)

	public_tweets = api.search('bitcoin')
	user = { 'nickname': 'Ryan' } #fake user


	#Tweet(tweet="tes tweet")
	return render_template("index.html", user=user, tweets=public_tweets)
