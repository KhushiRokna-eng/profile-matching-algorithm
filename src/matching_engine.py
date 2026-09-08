import pandas as pd

from preprocessing import preprocess_users
from text_similarity import create_tfidf_matrix, calculate_similarity
from mbti_logic import calculate_mbti_compatibility
from utils import calculate_location_compatibility
from scoring_engine import calculate_hybrid_score
from feedback_loop import calculate_acceptance_rate, calculate_adaptive_score

def load_and_prepare_users():
    """
    Load users and prepare their profile text for matching.
    """
    users = preprocess_users("data/users.csv")
    return users

def calculate_text_similarity(users):
    """
    Calculate text similarity between all user profiles.
    """
    vectorizer, tfidf_matrix = create_tfidf_matrix(users["cleaned_text"])
    similarity_matrix = calculate_similarity(tfidf_matrix)

    return similarity_matrix

def calculate_location_similarity(user1, user2):
    """
    Calculate location compatibility between two users.
    """
    return calculate_location_compatibility(
        user1["location"],
        user2["location"]
    )

def calculate_hybrid_similarity(user1, user2, text_score):
    """
    Calculate the final hybrid compatibility score.
    """
    mbti_score = calculate_mbti_similarity(user1, user2)
    location_score = calculate_location_similarity(user1, user2)

    hybrid_score = calculate_hybrid_score(
        text_score,
        mbti_score,
        location_score
    )

    return hybrid_score

def calculate_adaptive_similarity(user1, hybrid_score, feedback):
    """
    Adjust the hybrid score using the user's previous feedback.
    """
    acceptance_rate = calculate_acceptance_rate(
        feedback,
        user1["user_id"]
    )

    adaptive_score = calculate_adaptive_score(
        hybrid_score,
        acceptance_rate
    )

    return adaptive_score, acceptance_rate

def find_matches(target_user_id, users, similarity_matrix, feedback):
    """
    Find and rank the best matches for a target user.
    """
    target_indices = users.index[
        users["user_id"] == target_user_id
    ]
    
    if len(target_indices) == 0:
        raise ValueError(
            f"User ID {target_user_id} not found."
        )
        
    target_index = target_indices[0]

    matches = []

    for index, user in users.iterrows():

        # Do not match the user with themselves
        if user["user_id"] == target_user_id:
            continue

        text_score = similarity_matrix[target_index][index]

        mbti_score = calculate_mbti_similarity(
            users.loc[target_index],
            user
        )

        location_score = calculate_location_similarity(
            users.loc[target_index],
            user
        )

        location_score = calculate_location_similarity(
            users.loc[target_index],
            user
        )
    
        hybrid_score = calculate_hybrid_similarity(
            users.loc[target_index],
            user,
            text_score
        )

        adaptive_score, acceptance_rate = calculate_adaptive_similarity(
            users.loc[target_index],
            hybrid_score,
            feedback
        )

        matches.append({
            "user_id": user["user_id"],
            "name": user["name"],
            "text_score": text_score,
            "mbti_score": mbti_score,
            "location_score": location_score,
            "hybrid_score": hybrid_score,
            "acceptance_rate": acceptance_rate,
            "adaptive_score": adaptive_score
        })

    matches_df = pd.DataFrame(matches)

    matches_df = matches_df.sort_values(
        by="adaptive_score",
        ascending=False
    )

    return matches_df
   
def calculate_mbti_similarity(user1, user2):
    """
    Calculate MBTI compatibility between two users.
    """
    return calculate_mbti_compatibility(
        user1["mbti_type"],
        user2["mbti_type"]
    )
    
    
if __name__ == "__main__":
    users = load_and_prepare_users()

    similarity_matrix = calculate_text_similarity(users)

    feedback = pd.read_csv("data/feedback.csv")

    target_user_id = 50

    matches = find_matches(
        target_user_id,
        users,
        similarity_matrix,
        feedback
    )

    top_n = 10
    print(f"\nTop {top_n} matches for User {target_user_id}:")
    print(
        matches.head(top_n).to_string(index=False)
    )