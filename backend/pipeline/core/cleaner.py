# core/cleaner.py

import re
from config.mapping import CONDITION_MAPPING, CITY_MAPPING


def clean_text(text):
    """
    General text normalization for fields like name, address, email.

    - remove leading/trailing spaces
    - collapse multiple spaces
    """

    if not text:
        return ""

    text = text.strip()

    # replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    return text


def normalize_text(text):
    """
    Converts text to lowercase and strips extra spaces.
    Used before matching against mapping dictionaries.
    """

    if not text:
        return None

    return text.strip().lower()


def map_city(raw_city):
    """
    Maps messy city names to standardized city enum.
    """

    if not raw_city:
        return None

    city = normalize_text(raw_city)

    # Check mapping dictionary first
    if city in CITY_MAPPING:
        return CITY_MAPPING[city]

    # Otherwise return cleaned capitalized city
    return city.capitalize()


def map_conditions(raw_conditions):
    """
    Takes a list of raw condition strings
    Returns standardized condition list.
    """

    standardized = []

    for condition in raw_conditions:

        normalized = normalize_text(condition)

        if normalized in CONDITION_MAPPING:
            standardized.append(CONDITION_MAPPING[normalized])

        else:
            standardized.append(condition.upper())

    return list(set(standardized))  # remove duplicates


def clean_service(service):
    """
    Clean individual service record fields.
    """

    service["name"] = clean_text(service.get("name"))
    service["address"] = clean_text(service.get("address"))
    service["email"] = clean_text(service.get("email"))

    return service


def clean_dataset(services):
    """
    Apply cleaning to entire dataset.
    """

    cleaned = []

    for service in services:
        cleaned.append(clean_service(service))

    return cleaned