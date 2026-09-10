from src.utils import calculate_location_compatibility


def test_location_compatibility():
    assert calculate_location_compatibility("Jaipur", "Jaipur") == 1.0
    assert calculate_location_compatibility("Jaipur", "Pune") == 0.0
    assert calculate_location_compatibility("Pune", "pune") == 1.0
    assert calculate_location_compatibility(None, "Pune") == 0.0