from urllib2 import Request, urlopen, URLError
import urllib
import re
import urllib2
from bs4 import BeautifulSoup
from nltk.tag.stanford import NERTagger
from nltk.tag.stanford import POSTagger
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values={}
proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
headers={'User-Agent': user_agent}
data = urllib.urlencode(values)
req = Request("http://en.wikipedia.org/wiki/International_Institute_of_Information_Technology,_Hyderabad",data,headers)
try:
	response = urlopen(req)
	soup=BeautifulSoup(response.read())
	#p="p".encode(encoding="UTF")
	for para in soup.find_all('p'):
	 res=para.text
		
	 st = POSTagger('/usr/share/stanford-postagger/models/english-bidirectional-distsim.tagger',
			'/usr/share/stanford-postagger/stanford-postagger.jar')
	 try :
          print st.tag(res.split())
	 except :
          pass
	# print para
except URLError as e:
	if hasattr(e, 'reason'):
	  print 'We failed to reach a server.'
	  print 'Reason: ', e.reason
	 # print 'complete :',e.fp.read()
	elif hasattr(e, 'code'):
	  print 'The server couldn\'t fulfill the request.'
	  print 'Error code: ', e.code
	else:
	  print "everything is fine"
