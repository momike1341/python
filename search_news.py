#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests_oauthlib import OAuth1Session
import json
import time
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from naoqi import ALProxy


def news_search(news):
     url="https://news.google.com/news/search/section/q/"+news
     res=requests.get(url)
     s=BeautifulSoup(res.content,"html.parser")
     try:
         a=s.find("a",{"class":"nuEeue hzdq5d ME7ew"}).string.encode('utf-8')
     except:
         a=""
     return a


url= raw_input('>> '.encode("shift_jis"))
print  news_search(url)
