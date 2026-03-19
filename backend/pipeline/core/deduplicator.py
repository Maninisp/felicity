# core/deduplicator.py

def normalize_string(text):
    """
    Normalize text for comparison:
    - lowercase
    - remove extra spaces
    """
    if not text:
        return ""

    return " ".join(text.lower().split())


def generate_key(service):
    """
    Create a unique key for duplicate detection.
    Uses name + address combination.
    """

    name = normalize_string(service.get("name"))
    address = normalize_string(service.get("address"))

    return f"{name}|{address}"


def remove_duplicates(services):
    """
    Removes duplicate services based on generated key.
    """

    seen = set()
    unique_services = []

    for service in services:

        key = generate_key(service)

        if key not in seen:
            seen.add(key)
            unique_services.append(service)

    return unique_services