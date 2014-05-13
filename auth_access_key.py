import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key="a2tFuHSiKSQFDyWLdGuLQ"
consumer_secret="PvTZtYGshDTPoYBeYuyS5D5E3f4EGEhyAz819CSLGg"
auth=OAuthHandler(consumer_key,consumer_secret)
auth_url=auth.get_authorization_url()
print auth_url
verifier=raw_input('pin : ').strip()
auth.get_access_token(verifier)
api = tweepy.API(auth)
#print api.me(),auth.access_token.key,auth.access_token.secret
auth.set_access_token(auth.access_token.key, auth.access_token.secret)
msg="We expect @%s to be a person who holds views about topics of your interest,please follow him" %(locvar.screen_name)
puser=[1422717301]
for lociter in puser:
	yy=api.send_direct_message(user=lociter,text=msg)
	print yy							                    


 

