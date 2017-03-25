import os
import tweepy
import settings as s
from tweepy import OAuthHandler
from tweepy import Stream
from dm_listener import DMListener

if __name__ == '__main__':
    auth = OAuthHandler(s.TWITTER_CONSUMER_KEY, s.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(s.TWITTER_ACCESS_TOKEN, s.TWITTER_TOKEN_SECRET)
    api = tweepy.API(auth)

    stream = Stream(auth=auth, listener=DMListener())

    stream.userstream()
