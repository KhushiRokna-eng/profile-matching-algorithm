from src.mbti_logic import calculate_mbti_compatibility


def test_mbti_compatibility():
    assert calculate_mbti_compatibility("INTP", "INTP") == 1.0
    assert calculate_mbti_compatibility("INTP", "ENFP") == 0.5
    assert calculate_mbti_compatibility("INTP", "ESTJ") == 0.25