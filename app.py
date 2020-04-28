import tweepy
import time

api_key = "0nOI9Y1sg5xqgZQFneiTOKQn8"
api_secret = "oRe8VX4tyS5AP8h74nImtyLSE7r25aeuboq7BDjSLV6siRSfsq"

a_token = "1254538318722678785-DYSt4x1FBgKINsr1Pd0CDGEse6NTkA"
a_t_secret = "iQ1SbQYnJSPRN3m9blqZ3t8ZL82aW0AfYHJiSWwUqTQRl"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(a_token, a_t_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

key_words = "research data management"

nrTweets = 500

user = api.me()

for tweet in tweepy.Cursor(api.search, key_words).items(nrTweets):
    try:
        print("Retweet success!")
        tweet.retweet()
        time.sleep(300)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
