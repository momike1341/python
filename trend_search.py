#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests_oauthlib import OAuth1Session
import json
import time
import re
import requests
import pas
from bs4 import BeautifulSoup
from datetime import datetime
from naoqi import ALProxy


### Constants                                                                                                                                                     
oath_key_dict = pas.oath_key_dict       

keyword={}
keyword_list=[]




### Functions                                                                                                                                                     
def main():
    global tweet_idmax
    tweets = tweet_search(u"", oath_key_dict)
    keyword_list=keyword.keys()
    ct=tweets[0]["created_at"]
    t = datetime.strptime(ct,"%Y-%m-%dT%H:%M:%SZ")
    fl=0
    for tweet in tweets[0]["trends"]:
            if (tweet["name"] not in keyword_list):
                print tweet["name"]
                search = news_search(tweet["name"].encode('utf-8'))
                print search 
                fl=1
            else:
                if ((t-keyword[tweet["name"]]).total_seconds()>10*60*60):
                    print tweet["name"]
                    fl=1
            keyword.update ({tweet["name"]:t})
    return

def news_search(news):
    url="https://news.google.com/news/search/section/q/"+news
    res=requests.get(url)
    s=BeautifulSoup(res.content,"html.parser")
    try:
        a=s.find("a",{"class":"nuEeue hzdq5d ME7ew"}).string.encode('utf-8')
    except:
        a=""
    return a

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict):
    url = "https://api.twitter.com/1.1/trends/place.json"
    params = {
        "id":23424856       #日本のトレンド
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets


### Execute
if __name__ == "__main__":
    while(1):
        main()
        time.sleep(100)
