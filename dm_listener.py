import os
from tweepy.streaming import StreamListener
from slackclient import SlackClient

class DMListener(StreamListener):
    def __init__(self, api=None):
        super(DMListener, self).__init__(api=None)
        # setup slack client
        self.slack = SlackClient(os.environ.get('SLACK_API_TOKEN'))

    def on_direct_message(self, data):
        message = data._json.get('direct_message')

        # if dm from certain user, forward to slack channel
        if message['sender']['id_str'] == os.environ.get("TWITTER_ID"):
            self.slack.api_call(
                "chat.postMessage",
                channel=os.environ.get("SLACK_CHANNEL"),
                text=message['text']
            )
        else:
            print message['text']

        return True

    def on_error(self, status):
        print 'we has err'
        print status
