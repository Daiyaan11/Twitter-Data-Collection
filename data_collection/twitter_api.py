import time
import tweepy
import os
from dotenv import load_dotenv
from tweepy.errors import TooManyRequests

def collect_tweets(query, max_results=100):
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


# Load credentials from the .env file
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def collect_tweets(query: str, max_results: int = 10):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["author_id", "created_at", "text"]
        )
        time.sleep(1)  # Add a delay of 1 second between requests
        return response.data
    except tweepy.TooManyRequests as e:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(900)  # Wait for 15 minutes if rate limit is hit
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []