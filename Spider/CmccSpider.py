# coding: UTF-8
'''
Created on 2013年11月14日

@author: NOAH
'''

import urllib  
import urllib2  
  
def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()  
  



