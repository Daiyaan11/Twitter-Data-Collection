import csv
import json
import sys
import os
from data_collection.twitter_api import collect_tweets
from data_collection.preprocess import clean_text, tokenize_text
from analysis.hashtag_analysis import analyze_hashtags
from analysis.topic_modeling import extract_topics
from analysis.entity_analysis import extract_named_entities

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure the data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

def save_to_csv(file_name, data, headers=None):
    """Save data to a CSV file."""
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

def save_to_json(file_name, data):
    """Save data to a JSON file."""
    with open(file_name, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Define query and fetch tweets
query = "(#servicedelivery OR #municipality OR #eskom OR #citypower OR #joburgwater) lang:en"
tweets = collect_tweets(query, max_results=100)

# Preprocess tweets
cleaned_tweets = [clean_text(tweet.text) for tweet in tweets]

# Analyze hashtags and active users
top_hashtags, top_users = analyze_hashtags(tweets)

# Perform topic modeling
topics = extract_topics(cleaned_tweets)

# Perform named entity analysis on the first 10 tweets
entities = [extract_named_entities(tweet.text) for tweet in tweets[:10]]

try:
    tweets = collect_tweets(query, max_results=100)
    save_to_csv(tweets, "data/tweets.csv")
    save_to_json(tweets, "data/tweets.json")
except KeyboardInterrupt:
    print("Script manually stopped. Saving partial data...")
    save_to_csv(tweets, "data/tweets_partial.csv")
    save_to_json(tweets, "data/tweets_partial.json")
    print("Partial data saved.")


# Save results
save_to_csv("top_hashtags.csv", [(tag, count) for tag, count in top_hashtags], headers=["Hashtag", "Count"])
save_to_csv("top_users.csv", [(user_id, count) for user_id, count in top_users], headers=["User ID", "Tweet Count"])
save_to_json("topics.json", {"topics": topics})
save_to_json("entities.json", entities)

# Print summary
print("Top Hashtags:", top_hashtags)
print("Top Active Users:", top_users)
print("Topics:", topics)
print("Named Entities:", entities)
print("Cleaned Tweets:", cleaned_tweets)

print(f"Number of tweets collected: {len(tweets)}")
for tweet in tweets[:5]:  # Display the first 5 tweets for verification
    print(tweet)


# Save tweets to CSV and JSON
save_to_csv(tweets, "data/tweets.csv")
save_to_json(tweets, "data/tweets.json")
