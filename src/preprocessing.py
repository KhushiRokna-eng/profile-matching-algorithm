import re
import pandas as pd
from nltk.corpus import stopwords


STOP_WORDS = set(stopwords.words("english"))


def clean_text(text):
    """
    Clean a text string for NLP processing.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS]

    return " ".join(words)


def preprocess_users(file_path):
    """
    Load users.csv and create cleaned profile text.
    """

    df = pd.read_csv(file_path)

    # Combine the two text fields
    df["profile_text"] = (
        df["about_me"].fillna("") + " " +
        df["professional_summary"].fillna("")
    )

    # Clean the combined text
    df["cleaned_text"] = df["profile_text"].apply(clean_text)

    return df