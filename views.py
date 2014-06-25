from flask import render_template
from app import app
import tweepy

@app.route('/')
@app.route('/index')
def index():
	ckey='wuWgjIP9ouUWTeo0D3WcF1WZ0'
	csecret='KLjs8izSiuTDkHlOpjlFcrmxaJnQSMTqqckvxvVC2g1RMc5Gwo'
	atoken='615818947-y32PlOKg38iu4hMjcjV42u5fKJzSM1ixbpWoIibb'
	asecret='aDqKj6OlbrwqQ7zAGh8ONgPTn02p0k062zsGppiWJLv3U'

	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	api = tweepy.API(auth)

	public_tweets = api.search('bitcoin')
	user = { 'nickname': 'Ryan' } #fake user
	return render_template("index.html", user=user, tweets=public_tweets)
