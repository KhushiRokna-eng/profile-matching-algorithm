import pandas as pd

from src.feedback_loop import (
    calculate_acceptance_rate,
    calculate_adaptive_score
)


def test_acceptance_rate():
    feedback = pd.DataFrame({
        "user_id": [1, 1, 1, 2],
        "matched_user_id": [2, 3, 4, 1],
        "action": [1, 0, 1, 0]
    })

    assert calculate_acceptance_rate(feedback, 1) == 2 / 3
    assert calculate_acceptance_rate(feedback, 999) == 0.0


def test_adaptive_score():
    score = calculate_adaptive_score(0.5, 0.5)

    assert abs(score - 0.5) < 1e-6