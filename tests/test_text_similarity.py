from src.text_similarity import create_tfidf_matrix, calculate_similarity


def test_text_similarity():
    texts = [
        "machine learning engineer",
        "machine learning developer",
        "graphic designer"
    ]

    vectorizer, tfidf_matrix = create_tfidf_matrix(texts)
    similarity_matrix = calculate_similarity(tfidf_matrix)

    assert tfidf_matrix.shape[0] == 3
    assert similarity_matrix.shape == (3, 3)
    assert abs(similarity_matrix[0][0] - 1.0) < 1e-6