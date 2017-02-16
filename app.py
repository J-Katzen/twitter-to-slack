import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from dm_listener import DMListener

if __name__ == '__main__':
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    token_secret = os.environ.get('TWITTER_TOKEN_SECRET')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth)

    stream = Stream(auth=auth, listener=DMListener())

    stream.userstream()
