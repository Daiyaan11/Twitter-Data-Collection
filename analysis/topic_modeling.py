# analysis/topic_modeling.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(cleaned_tweets, num_topics=5):
    if not cleaned_tweets or all(len(tweet.strip()) == 0 for tweet in cleaned_tweets):
        print("No valid tweets to process for topic modeling.")
        return []

    vectorizer = CountVectorizer(stop_words="english", max_features=1000)
    text_matrix = vectorizer.fit_transform(cleaned_tweets)

    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(text_matrix)

    topics = []
    for idx, topic in enumerate(lda.components_):
        topic_keywords = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics.append({"Topic": idx + 1, "Keywords": topic_keywords})

    return topics
