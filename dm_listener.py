# @j-katzen
import os
import re
import settings as s
from tweepy.streaming import StreamListener
from slackclient import SlackClient

class DMListener(StreamListener):
    def __init__(self, api=None):
        super(DMListener, self).__init__(api=None)
        # setup slack client
        self.slack = SlackClient(s.SLACK_API_TOKEN)

    def on_status(self, data):
        sender = data._json.get("user")
        message = data._json.get("text")
        has_bitcoin_tag = True if "#bitcoin" in message["text"] else False

        if sender["id_str"] == s.TWITTER_ID and has_bitcoin_tag:
            icon = ":reddie:" if "#altsaredead" in message["text"] else ":greenie:"
            self.slack.api_call(
                "chat.postMessage",
                channel=s.SLACK_CHANNEL,
                username='Coindata',
                as_user=False,
                test=message["text"],
                icon_emoji=icon
            )

        return True

    def on_direct_message(self, data):
        message = data._json.get("direct_message")

        # if dm from certain user, forward to slack channel
        if message["sender"]["id_str"] == s.TWITTER_ID:
            self.slack.api_call(
                "chat.postMessage",
                channel=s.SLACK_CHANNEL,
                text=message['text'],
                username='Coindata',
                as_user=False,
                icon_emoji=':greenie:'
            )
        else:
            print message["text"]

        return True

    def on_error(self, status):
        print "we has err"
        print status
