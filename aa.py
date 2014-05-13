# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
#from gluon.contrib.login_methods.oauth10a_account import OAuthAccount
consumer_token="a2tFuHSiKSQFDyWLdGuLQ"
consumer_secret="PvTZtYGshDTPoYBeYuyS5D5E3f4EGEhyAz819CSLGg"
 
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import string
import sys
import time

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
	def on_error(self, status):
		print status
     

def twitauth():
    auth=OAuthHandler(consumer_token,consumer_secret,"http://127.0.0.1:8000/high_on_twitter/default/callback")
    auth_url=auth.get_authorization_url()
    print "auth_url",auth_url
    aa={}
    aa['key']=auth.request_token.key
    aa['secret']=auth.request_token.secret
    session.request_token=aa
    print "request-token,key,secret twitauth",auth.request_token.key,auth.request_token.secret
    #session.set('request_token', (auth.request_token.key,auth.request_token.secret))
    redirect(auth_url)
    '''print auth_url
    verifier=raw_input('pin : ').strip()
    auth.get_access_token(verifier)
    api = tweepy.API(auth)
    print api.me(),auth.access_token.key,auth.access_token.secret
    auth.set_access_token(auth.access_token.key, auth.access_token.secret)
    '''
   
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()"""
    
    return dict(message=T('Hqello World'))
    
def getmeloc(cood): ## auxillary function to get tweet author location based on his last tweet
    aa={}
    aa["loclong"]=0.0 #default value centre of earth
    aa["loclat"]=0.0
    if cood!=None:
        aa["loclong"]=cood.coordinates[0]
        aa["loclat"]=cood.coordinates[1]
    else:
        return None
    return aa

    
        
                
def callback():
    chk=0
    form = SQLFORM.factory(Field('chk','boolean',required=True,label='Have created the application on application behalf'))
    if form.accepts(request.vars,session):
        chk=form.vars.chk
    elif form.errors:
        response.flash='Errors in form'
    print "oauth verifier-",request['get_vars']['oauth_verifier']
    verifier=request['get_vars']['oauth_verifier']
    #verifier = request.GET.get('oauth_verifier')
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    token = session.get('request_token')
    print "token",token
    #session.delete('request_token')
    auth.set_request_token(token['key'], token['secret'])
    
    try:
        auth.get_access_token(verifier)
        auth.set_access_token(auth.access_token.key, auth.access_token.secret)
        api = tweepy.API(auth)
        locvar=api.me()
        loclong=None
        loclat=None
        try:
            locstat=locvar.status
            try :
                loccod=getmeloc(locvar.status.coordinates)
                if loccod!=None:
                    loclong=loccod["loclong"]
                    loclat=loccod["loclat"]
            except TypeError:
                loclong=0.0
                loclat=0.0
        except AttributeError:
            pass
        query=db((db.myuser.access_public==auth.access_token.key) & (db.myuser.access_secret==auth.access_token.secret)).select()
        if(len(query)==0):
            db.myuser.insert(pid=locvar.id,descrp=locvar.description, myscrname=locvar.screen_name,longi=loclong,lati=loclat,accbyme=chk,access_public=auth.access_token.key,access_secret=auth.access_token.secret)
            session.response="Registered successfully"
        else:
            session.response='Already registered'
        redirect(URL('index'))
            
        print type(locvar.status.coordinates),auth.access_token.key,auth.access_token.secret
    except tweepy.TweepError:
        session.response="Sorry Can Not Register You"
    return dict(form=form)    
     
     
def followmyusers():
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
    myaccess_token="255119068-hEIypjzq6RdNkNJk4RTuZtSLOVHuEyMMRWYoQniD"#my own tokens
    myaccess_token_secret="rFnq8QGgcplvhLx8O56W2CVYgRPixSaUxIcUHWwjY"
    l = StdOutListener()
    ulauth= OAuthHandler(consumer_token, consumer_secret)
    ulauth.set_access_token(myaccess_token,myaccess_token_secret)
    stream = Stream(ulauth, l)
    #stream.sample()
    query=db((db.myuser.id>0) & (db.myuser.accbyme==False)).select(db.myuser.pid)
    l=[] ## list of ids of all app users to follow
    for i in query:
        l.append(i.pid)    
    print "asdf"
    #stream.filter(track=l)
	print "hey b2"
	     

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
