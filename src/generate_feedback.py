import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Configuration
# -----------------------------

INPUT_FILE = "data/users.csv"
OUTPUT_FILE = "data/feedback.csv"

INTERACTIONS_PER_USER = 7
RANDOM_SEED = 42

random.seed(RANDOM_SEED)


# -----------------------------
# Load user profiles
# -----------------------------

df = pd.read_csv(INPUT_FILE)

# Combine the two text fields used for profile similarity
df["combined_text"] = (
    df["about_me"].fillna("") + " " +
    df["professional_summary"].fillna("")
)


# -----------------------------
# Calculate text similarity
# -----------------------------

vectorizer = TfidfVectorizer(stop_words="english")

text_vectors = vectorizer.fit_transform(df["combined_text"])

similarity_matrix = cosine_similarity(text_vectors)


# -----------------------------
# MBTI similarity
# -----------------------------

def mbti_similarity(type_a, type_b):
    """
    Compare two MBTI types by counting
    how many of their four letters match.

    Returns a value between 0 and 1.
    """

    return sum(
        a == b
        for a, b in zip(type_a, type_b)
    ) / 4


# -----------------------------
# Generate feedback
# -----------------------------

feedback_records = []

user_ids = df["user_id"].tolist()

for i, user_id in enumerate(user_ids):

    # Possible users to match with
    possible_users = [
        uid for uid in user_ids
        if uid != user_id
    ]

    # Select unique candidate profiles
    matched_users = random.sample(
        possible_users,
        INTERACTIONS_PER_USER
    )

    for matched_user_id in matched_users:

        # Find index of matched user
        matched_index = df.index[
            df["user_id"] == matched_user_id
        ][0]

        # Text similarity
        text_score = similarity_matrix[i][matched_index]

        # MBTI similarity
        mbti_score = mbti_similarity(
            df.iloc[i]["mbti_type"],
            df.iloc[matched_index]["mbti_type"]
        )

        # Location similarity
        location_score = int(
            df.iloc[i]["location"]
            == df.iloc[matched_index]["location"]
        )

        # Combined compatibility score
        compatibility_score = (
            0.65 * text_score
            + 0.20 * mbti_score
            + 0.15 * location_score
        )

        # Convert compatibility into probability
        acceptance_probability = (
            0.15
            + 0.70 * compatibility_score
        )

        # Generate synthetic feedback
        action = int(
            random.random() < acceptance_probability
        )

        feedback_records.append({
            "user_id": user_id,
            "matched_user_id": matched_user_id,
            "action": action,
            "timestamp": pd.Timestamp.now()
        })


# -----------------------------
# Create feedback dataframe
# -----------------------------

feedback_df = pd.DataFrame(feedback_records)

# Remove helper column from original dataframe
df.drop(columns=["combined_text"], inplace=True)

# Save feedback dataset
feedback_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# -----------------------------
# Display summary
# -----------------------------

print("Feedback dataset generated successfully!")
print("Shape:", feedback_df.shape)

print("\nColumns:")
print(feedback_df.columns.tolist())

print("\nAction distribution:")
print(feedback_df["action"].value_counts())

print("\nInteractions per user:")
print(feedback_df["user_id"].value_counts().describe())

print("\nSaved to:", OUTPUT_FILE)