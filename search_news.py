#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#from requests_oauthlib import OAuth1Session
import json
import requests
from bs4 import BeautifulSoup
import re

def news_search(news):
     url="https://news.google.com/news/search/section/q/"+unicode(news)
     res=requests.get(url)
     s=BeautifulSoup(res.content,"html.parser")
     try:
         a=s.find("a",{"class":"nuEeue hzdq5d ME7ew"}).string.encode('utf-8')
     except:
         a=""
     return a

search_word= raw_input('>> ')
print  news_search(search_word)
