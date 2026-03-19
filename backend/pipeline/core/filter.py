# core/filter.py

TARGET_CITIES = ["mumbai", "pune", "bangalore"]


def is_target_city(service):
    """
    Check if service belongs to our target cities.
    We check both city (district) and address.
    """

    city = service.get("city", "").lower()
    address = service.get("address", "").lower()

    for target in TARGET_CITIES:
        if target in city or target in address:
            return True

    return False


def filter_by_city(services):
    """
    Filters dataset to only include target cities.
    """

    filtered = []

    for service in services:
        if is_target_city(service):
            filtered.append(service)

    return filtered