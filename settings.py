# @j-katzen
#
from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_ID = environ.get("TWITTER_ID")
TWITTER_CONSUMER_KEY = environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_TOKEN_SECRET = environ.get("TWITTER_TOKEN_SECRET")
SLACK_API_TOKEN = environ.get("SLACK_API_TOKEN")
SLACK_CHANNEL = environ.get("SLACK_CHANNEL")
