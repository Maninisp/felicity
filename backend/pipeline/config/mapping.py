# config/mapping.py

# All keys should be lowercase for matching

CONDITION_MAPPING = {
    # ADHD umbrella
    "attention deficit disorder": "ADHD",
    "add": "ADHD",
    "attention deficit hyperactivity disorder": "ADHD",

    # Autism umbrella
    "asd": "Autism",
    "autism spectrum disorder": "Autism",
    "spectrum disorder": "Autism",

    # Cognitive Delay umbrella
    "intellectual disability": "Cognitive Delay",
    "global developmental delay": "Cognitive Delay",
    "developmental delay": "Cognitive Delay",

    # Blindness umbrella
    "visual impairment": "Blindness",
    "low vision": "Blindness",

    # Deafness umbrella
    "hearing impairment": "Deafness",
    "hard of hearing": "Deafness"
}

CITY_MAPPING = {
    "bombay": "Mumbai",
    "mumbai city": "Mumbai",
    "mumbai suburban": "Mumbai",
    "mumbai": "Mumbai",
    "bengaluru urban": "Bangalore",
    "bangalore": "Bangalore",
    "bengaluru": "Bangalore",
    "pune": "Pune"
}