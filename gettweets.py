import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import string
import sys
import time
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
		#for i in t.keys():
		#	print i,t[i]
		#print type(t)
		a="text"
		a=a.encode("ascii","ignore")
		try:
			txt=t[a].encode("ascii",'ignore')
			print txt
		except KeyError:
			pass
		
		return True
	def on_status(self,status):
		print type(status),dir(status)
		return True
	def on_error(self, status):
		print status

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.sample()
#api = tweepy.API(auth)
#o=api.me()
#print o.id,o.screen_name

#api.update_status('hello world')
#stream.filter(track=["obama"])
#for k in range(4):
#	time.sleep(4)
#	t=api.search("iiit")
#	for i in t:
##		print i.user.screen_name,i.text
	
