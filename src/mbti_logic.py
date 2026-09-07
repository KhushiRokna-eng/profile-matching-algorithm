def calculate_mbti_compatibility(mbti1, mbti2):
    """
    Calculate MBTI compatibility based on matching dimensions.

    Returns a score between 0 and 1.
    """

    # Convert to uppercase
    mbti1 = mbti1.upper()
    mbti2 = mbti2.upper()

    # Validate MBTI length
    if len(mbti1) != 4 or len(mbti2) != 4:
        raise ValueError("MBTI types must contain exactly 4 characters.")

    # Count matching dimensions
    matches = sum(a == b for a, b in zip(mbti1, mbti2))

    # Convert matches to a score between 0 and 1
    compatibility_score = matches / 4

    return compatibility_score