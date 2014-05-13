l=[]
l.append(["255119068-hEIypjzq6RdNkNJk4RTuZtSLOVHuEyMMRWYoQniD","rFnq8QGgcplvhLx8O56W2CVYgRPixSaUxIcUHWwjY"])
l.append(["1422717301-yj0a8BgRT5ruFo9gwfhE2ArvOHxPpwr1y0oIEd3","ZTpp9G8RG4TDnDUd63CO2W1uQ5qJFmPnPp5ypqACA"])
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="a2tFuHSiKSQFDyWLdGuLQ"
consumer_secret="PvTZtYGshDTPoYBeYuyS5D5E3f4EGEhyAz819CSLGg"
###############################################################making faisal rishabh's follower
'''a="rishabhgunner27"
b="faisaliiit"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(l[1][0], l[1][1])
api=tweepy.API(auth)
q=api.create_friendship(a)
if(type(q)):
  print "hurrey"
else:
 print "ohmy"'''

###############################################################sending faisal direct message

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(l[0][0], l[0][1])
api=tweepy.API(auth)
auth1 = OAuthHandler(consumer_key, consumer_secret)#rishabh
auth1.set_access_token(l[1][0], l[1][1])
qapi=tweepy.API(auth1)
#print dir(qapi.me())
msg="aya kya"
yy=qapi.send_direct_message(user=1931034948,text=msg)
if(type(yy)):
  print "msg sent hurrey"
else:
 print "no ohmy"

