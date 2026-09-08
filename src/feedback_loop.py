def calculate_acceptance_rate(feedback, user_id):
    """
    Calculate the acceptance rate for a user.

    Acceptance rate = accepted interactions / total interactions.
    """

    user_feedback = feedback[feedback["user_id"] == user_id]

    if len(user_feedback) == 0:
        return 0.0

    acceptance_rate = user_feedback["action"].mean()

    return acceptance_rate

def calculate_adaptive_score(hybrid_score, acceptance_rate):
    """
    Adjust the hybrid score using previous user feedback.

    Hybrid profile compatibility contributes 80%.
    Historical acceptance rate contributes 20%.
    """

    adaptive_score = (
        0.80 * hybrid_score
        + 0.20 * acceptance_rate
    )

    return adaptive_score