import tweepy
import os
import sys

def main():

    api_key = sys.argv[0]
    api_key_secret = sys.argv[1]
    access_token = sys.argv[2]
    access_token_secret = sys.argv[3]
    status = sys.argv[4]
# api_key_secret, access_token, access_token_secret, status = sys.argv[1:]

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    print(api_key)  # Print the API key to verify it's received correctly

    tweet_content = status  # Use the 'status' input variable
    client.create_tweet(text = tweet_content)

    # Now you can use the 'tweet_content' and 'client' objects as needed in your script.

if __name__ == "__main__":
    main()
