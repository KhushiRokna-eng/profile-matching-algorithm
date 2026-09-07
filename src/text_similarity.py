from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_tfidf_matrix(texts):
    """
    Convert cleaned profile texts into TF-IDF vectors.
    """

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(texts)

    return vectorizer, tfidf_matrix

def calculate_similarity(tfidf_matrix):
    """
    Calculate cosine similarity between all profile vectors.
    """

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix