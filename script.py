import tweepy
import os

client = tweepy.Client(
    consumer_key=os.environ.get("api_key"),
    consumer_secret=os.environ.get("api_key_secret"),
    access_token=os.environ.get("access_token"),
    access_token_secret=os.environ.get("access_token_secret")
)
print(os.environ.get("api_key"))
tweet_content = "{{ inputs.status }}"
# client.create_tweet(text = tweet_content)
