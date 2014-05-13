import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import string
import sys
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="a2tFuHSiKSQFDyWLdGuLQ"
consumer_secret="PvTZtYGshDTPoYBeYuyS5D5E3f4EGEhyAz819CSLGg"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="255119068-hEIypjzq6RdNkNJk4RTuZtSLOVHuEyMMRWYoQniD"
access_token_secret="rFnq8QGgcplvhLx8O56W2CVYgRPixSaUxIcUHWwjY"

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream.
	    This is a basic listener that just prints received tweets to stdout.

	    """
	def on_data(self, data):
		data=data.encode("ascii","ignore")
		#print data["text"]
		
		t=json.loads(data)
		#print t
		#print t.keys()
		for i in t.keys():
	 		print i,t[i]
		#print type(t)
		txt=t["text"].encode("ascii",'ignore')
		print txt
		return True
	def on_error(self, status):
		print status

#l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#stream = Stream(auth, l)
#stream.sample()
api = tweepy.API(auth)
#api.update_status('hello world')
qt=api.home_timeline()
for i in qt:
	print i.text,i.retweet_count
# If the authentication was successful, you should
# see the name of the account print out
#print api.me().id
#print stream.firehose()
#l.on_data(stream)
#stream.filter(track=["iiit"])
#public_tweets = tweepy.api.me
#print public_tweets

#for tweet in public_tweets:
#	    print tweet.text
