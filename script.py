import tweepy
import os

client = tweepy.Client(
    consumer_key="{{ inputs.api_key }}",
    consumer_secret="{{ inputs.api_key_secret }}",
    access_token="{{ inputs.access_token }}",
    access_token_secret="{{ inputs.access_token_secret }}"
)

tweet_content = status = "{{ inputs.status }}"
client.create_tweet(text = tweet_content)
