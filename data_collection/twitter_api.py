import time
import tweepy
import os
from dotenv import load_dotenv
from tweepy.errors import TooManyRequests

# Load credentials from the .env file
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def collect_tweets(query: str, max_results: int = 10):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    tweets = []
    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["author_id", "created_at", "text"]
        )
        tweets.extend(response.data)
    except TooManyRequests:
        print("Rate limit exceeded. Waiting for 15 minutes...")
        time.sleep(15 * 60)  # Wait for 15 minutes before retrying
    return tweets
