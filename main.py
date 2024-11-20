from data_collection.twitter_api import collect_tweets
from data_collection.preprocess import clean_text
from analysis.hashtag_analysis import analyze_hashtags
from analysis.topic_modeling import extract_topics

# Define your query and max number of tweets to retrieve
query = "(#servicedelivery OR #municipality OR #eskom OR #citypower OR #joburgwater) lang:en place:Johannesburg"
max_results = 100

# Step 1: Collect tweets from Twitter API
tweets = collect_tweets(query, max_results)

# Step 2: Preprocess the collected tweets (cleaning the text)
cleaned_tweets = [clean_text(tweet.text) for tweet in tweets]

# Step 3: Analyze hashtags and active users
top_hashtags, top_users = analyze_hashtags(tweets)

# Step 4: Extract topics using LDA
topics = extract_topics(cleaned_tweets)

# Print results
print("Top Hashtags:", top_hashtags)
print("Top Active Users:", top_users)
print("Top Topics:")
for idx, topic in enumerate(topics):
    print(f"Topic {idx + 1}: {', '.join(topic)}")
