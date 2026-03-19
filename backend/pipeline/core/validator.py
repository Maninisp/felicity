# core/validator.py

from config.enums import (
    ALLOWED_CITIES,
    ALLOWED_CONDITIONS,
    ALLOWED_CATEGORIES,
    ALLOWED_SERVICE_TYPES
)


def validate_service(service):
    """
    Validates a cleaned service dictionary.
    Returns (True, None) if valid.
    Returns (False, error_message) if invalid.
    """

    # Required fields
    required_fields = ["name", "city", "category"]

    for field in required_fields:
        if not service.get(field):
            return False, f"Missing required field: {field}"

    # Enum validations
    if service["city"] not in ALLOWED_CITIES:
        return False, f"Invalid city: {service['city']}"

    if service["category"] not in ALLOWED_CATEGORIES:
        return False, f"Invalid category: {service['category']}"

    if service.get("service_type") and service["service_type"] not in ALLOWED_SERVICE_TYPES:
        return False, f"Invalid service type: {service['service_type']}"

    # Validate conditions
    for condition in service.get("conditions", []):
        if condition not in ALLOWED_CONDITIONS:
            return False, f"Invalid condition: {condition}"

    return True, None