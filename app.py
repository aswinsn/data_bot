import tweepy
import time
import os
from os import environ

api_key = environ["api_key"]
api_secret = environ["api_secret"]

a_token = environ["a_token"]
a_t_secret = environ["a_t_secret"]

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(a_token, a_t_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

key_words = "FAIRdata" or "datamanagement" or "researchdata" or "OpenScience"

nrTweets = 800

user = api.me()

for tweet in tweepy.Cursor(api.search, key_words).items(nrTweets):
    try:
        print("Retweet success!")
        tweet.retweet()
        time.sleep(120)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

##END###
