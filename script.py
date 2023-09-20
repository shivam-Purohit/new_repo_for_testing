import tweepy
import os
import sys

    api_key = sys.argv[1]
    api_key_secret = sys.argv[2]
    access_token = sys.argv[3]
    access_token_secret = sys.argv[4]
    status = sys.argv[5]
# api_key_secret, access_token, access_token_secret, status = sys.argv[1:]

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    print("is this printing")
    print(api_key)  # Print the API key to verify it's received correctly

    tweet_content = status  # Use the 'status' input variable
    client.create_tweet(text = tweet_content)

    # Now you can use the 'tweet_content' and 'client' objects as needed in your script.

