from collections import Counter
import re

def extract_hashtags(text):
    """Extract hashtags from text."""
    return re.findall(r"#\w+", text)

def analyze_hashtags(tweets):
    """Analyze hashtags and most active users from tweets."""
    hashtags = Counter()
    user_ids = Counter()
    
    for tweet in tweets:
        hashtags.update(extract_hashtags(tweet.text))
        user_ids[tweet.author_id] += 1
    
    return hashtags.most_common(10), user_ids.most_common(10)
