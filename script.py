import tweepy

client = tweepy.Client(
    consumer_key="{{ inputs.api_key }}",
    consumer_secret="{{ inputs.api_key_secret }}",
    access_token="{{ inputs.access_token }}",
    access_token_secret="{{ inputs.access_token_secret }}"
)
print(f"{input.api_key}")
tweet_content = "{{ inputs.status }}"
# client.create_tweet(text = tweet_content)
