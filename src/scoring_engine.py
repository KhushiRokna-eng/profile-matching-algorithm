def calculate_hybrid_score(text_score, mbti_score, location_score):
    """
    Calculate the final hybrid compatibility score.

    The score combines:
    - Text similarity: 65%
    - MBTI compatibility: 20%
    - Location compatibility: 15%

    Returns a score between 0 and 1.
    """

    hybrid_score = (
        0.65 * text_score
        + 0.20 * mbti_score
        + 0.15 * location_score
    )

    return hybrid_score