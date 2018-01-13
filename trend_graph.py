#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from requests_oauthlib import OAuth1Session
import json
import time
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import collections
import itertools
import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt
from time import sleep
import pas

oath_key_dict = pas.oath_key_dict


tags_list = []
hashtag = []
i={}
since_id = -1
max_id = -1

def main():
    get_trend()

def get_trend():
    global since_id,max_id
    tweets = tweet_search(u"#けもフレ exclude:retweets", oath_key_dict,since_id)
    for tweet in tweets["statuses"]:
        hashtag = []
        tweet_id = long(tweet[u'id_str'])
        if since_id==-1 or tweet_id<since_id:
            since_id=tweet_id
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']

        print "tweet_id:", tweet_id
        print "text:", text
        print "created_at:", created_at
        print "user_id:", user_id
        print "user_desc:", user_description
        print "screen_name:", screen_name
        print "user_name:", user_name

        for i in tweet[u'entities'][u'hashtags']:
            tags = i[u'text']
            print "hashtag:",tags
            hashtag.append(tags)
        tags_list.append(hashtag)
        print ""
    since_id=since_id-1
    



def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word, oath_key_dict,oldest_id):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": unicode(search_word),
        "lang": "ja",
        "result_type": "recent",
        "count": "25"
        }

    if oldest_id != -1:
        params['max_id'] = oldest_id
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets


if __name__ == "__main__":
    for k in [1,2]:
        main()
        print "\n\n"
        sleep(10)
