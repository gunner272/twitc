import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="a2tFuHSiKSQFDyWLdGuLQ"
consumer_secret="PvTZtYGshDTPoYBeYuyS5D5E3f4EGEhyAz819CSLGg"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="255119068-hEIypjzq6RdNkNJk4RTuZtSLOVHuEyMMRWYoQniD"
access_token_secret="rFnq8QGgcplvhLx8O56W2CVYgRPixSaUxIcUHWwjY"

#public_tweets = tweepy.API.public_timeline()
#for tweet in public_tweets:
#	    print tweet.text
# these are tokens of team27iiith@yahoo.in
'''consumer_key="3hnk5MLgGLABwaAwMQxQA"
consumer_secret="lzTL6HbWJwgWg8DTr3oTkSiZlxnabG0lZJp1aoWA"
access_token="2193589304-QfF6FEvJpTp8rHWfjd5pn4EjTQcDwii5iS2RJtF"
access_token_secret="yarLuLYYk5OKhYgzShjfFwIsw0MLDmLlgOlVU4Yp4WUlX"
'''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
qq=tweepy.API(auth)
#print qq.me().id_str
#p=qq.search('#arsenal')
qq.create_friendship(2193589304)


'''p=[255119068,1916845218,1422717301,1931034948]
for i in p:
 l=qq.user_timeline(i)
 #print type(l[0].user),dir(l[0]),l[0].user.name,l[0].user.screen_name
 for j in l:
	 print j.text
 print "aa"
'''

 #user=qq.get_user(i)
 #print user.screen_name
#print dir(p)

##***************LIST OF SCREEN NAME FOLLOWED BY ARGUEMENT(Screen name) TO get_user function
#print user.screen_name
#print user.followers_count
#for friend in user.friends():
#	   print friend.screen_name
	    
