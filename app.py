import tweepy
import time

api_key = ""
api_secret = ""

a_token = ""
a_t_secret = ""

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(a_token, a_t_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

key_words = "research data management" or "FAIR data" or "FAIR principles"

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
