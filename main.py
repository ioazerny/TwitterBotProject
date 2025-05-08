import tweepy
import os

# Load Twitter API credentials (use environment variables or temporarily hardcode)
consumer_key = os.getenv("TWITTER_CONSUMER_KEY") or "your_consumer_key"
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET") or "your_consumer_secret"
access_token = os.getenv("TWITTER_ACCESS_TOKEN") or "your_access_token"
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET") or "your_access_token_secret"
bearer_token = os.getenv("TWITTER_BEARER_TOKEN") or "your_bearer_token"

# Initialize Tweepy Client (API v2)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def post_tweet():
    """Posts a simple tweet"""
    try:
        response = client.create_tweet(text="Hello Twitter! This is my first bot tweet using API v2.")
        print(f"✅ Tweet posted! ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"❌ Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet()
