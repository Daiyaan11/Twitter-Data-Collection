from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(cleaned_tweets, num_topics=5):
    """Perform LDA topic modeling on cleaned tweets."""
    vectorizer = CountVectorizer(max_features=1000, stop_words="english")
    text_matrix = vectorizer.fit_transform(cleaned_tweets)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(text_matrix)
    
    topics = []
    for idx, topic in enumerate(lda.components_):
        topics.append([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
    
    return topics
