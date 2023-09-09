import tweepy
import os
import sys

def main():

    api_key, api_key_secret, access_token, access_token_secret, status = sys.argv[1:]

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    print(api_key)  # Print the API key to verify it's received correctly

    tweet_content = status  # Use the 'status' input variable

    # Now you can use the 'tweet_content' and 'client' objects as needed in your script.

if __name__ == "__main__":
    main()
