from src.preprocessing import clean_text


def test_clean_text():
    text = "I am a Machine Learning Engineer! I love building AI products."

    result = clean_text(text)

    assert result == "machine learning engineer love building ai products"