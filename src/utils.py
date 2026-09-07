import pandas as pd


def calculate_location_compatibility(location1, location2):
    """
    Calculate location compatibility.

    Returns 1.0 if both users are from the same location,
    otherwise returns 0.0.
    """

    # Handle missing locations
    if pd.isna(location1) or pd.isna(location2):
        return 0.0

    # Convert locations to lowercase and remove extra spaces
    location1 = str(location1).strip().lower()
    location2 = str(location2).strip().lower()

    if location1 == location2:
        return 1.0

    return 0.0