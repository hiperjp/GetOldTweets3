#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import GetOldTweets3 as got

def test_Username():
    tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama')\
                                               .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    assert tweet.username == 'BarackObama'

def test_QuerySearch():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#europe #refugees')\
                                               .setSince("2015-05-01")\
                                               .setUntil("2015-09-30")\
                                               .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    assert '#europe' in tweet.hashtags.lower()
    assert '#refugees' in tweet.hashtags.lower()

def test_QuerySearchForNativeRetweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('cencosud')\
                                               .setSince("2019-07-02")\
                                               .setUntil("2019-07-03")\
                                               .setMaxTweets(5)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        print("- ID: {} | RT ID: {} | {}".format(tweet.id, tweet.retweet_id, tweet.text))
