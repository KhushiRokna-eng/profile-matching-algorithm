from src.scoring_engine import calculate_hybrid_score


def test_hybrid_score():
    assert calculate_hybrid_score(1.0, 1.0, 1.0) == 1.0
    assert calculate_hybrid_score(0.0, 0.0, 0.0) == 0.0

    score = calculate_hybrid_score(0.8, 0.75, 1.0)

    assert abs(score - 0.82) < 1e-6