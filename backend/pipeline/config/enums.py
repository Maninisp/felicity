# config/enums.py

# These are the ONLY allowed values in the system.
# Validation layer will enforce these strictly.

ALLOWED_CITIES = [
    "Mumbai",
    "Pune",
    "Bangalore"
]

ALLOWED_CONDITIONS = [
    "ADHD",
    "Autism",
    "Cognitive Delay",
    "Blindness",
    "Deafness"
]

ALLOWED_CATEGORIES = [
    # Support
    "Doctor",
    "Therapist",
    "Medical Support Service",
    "Financial Aid Center",
    "Parent Support Group",

    # Training
    "Therapy Training Program",
    "Skill Development Program",
    "Special Education Training",
    "Parent Guidance Program",

    # Links
    "NGO",
    "Special School",
    "Resource Center",
    "Government Scheme",
    "Awareness Organization"
]

ALLOWED_SERVICE_TYPES = ["Online", "Offline", "Hybrid"]