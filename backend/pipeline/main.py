# backend/pipeline/main.py

import json
import os

from scraper.national_trust import scrape
from core.cleaner import clean_dataset, map_city, map_conditions
from core.filter import filter_by_city
from core.validator import validate_service
from core.deduplicator import remove_duplicates
from pipeline.db.insert_services import insert_services


BASE_DIR = os.path.dirname(__file__)


def run_pipeline():

    # -------------------------
    # STEP 1: SCRAPE
    # -------------------------
    services = scrape()
    print("Total services scraped:", len(services))

    raw_dir = os.path.join(BASE_DIR, "raw_data")
    os.makedirs(raw_dir, exist_ok=True)

    raw_path = os.path.join(raw_dir, "national_trust_raw.json")

    with open(raw_path, "w") as f:
        json.dump(services, f, indent=2)

    print("Raw data saved.")

    # -------------------------
    # STEP 2: LOAD RAW DATA
    # -------------------------
    with open(raw_path, "r") as f:
        raw_data = json.load(f)

    # -------------------------
    # STEP 3: CLEAN DATA
    # -------------------------
    cleaned_data = clean_dataset(raw_data)

    # -------------------------
    # STEP 4: MAPPING (standardization)
    # -------------------------
    for item in cleaned_data:
        item["city"] = map_city(item.get("city"))
        item["conditions"] = map_conditions(item.get("conditions", []))
        item["category"] = item.get("category", "").strip()

    # -------------------------
    # DEBUG (compare before vs after)
    # -------------------------
    print("\n--- DEBUG: CITY MAPPING CHECK ---")
    for i in range(min(10, len(cleaned_data))):
        print("RAW:", raw_data[i].get("city"))
        print("MAPPED:", cleaned_data[i].get("city"))
        print("---")

    print("Cleaned records:", len(cleaned_data))

    # -------------------------
    # SAVE CLEANED DATA
    # -------------------------
    processed_dir = os.path.join(BASE_DIR, "processed_data")
    os.makedirs(processed_dir, exist_ok=True)

    processed_path = os.path.join(processed_dir, "national_trust_cleaned.json")

    with open(processed_path, "w") as f:
        json.dump(cleaned_data, f, indent=2)

    print("Processed data saved.")

    # -------------------------
    # STEP 5: FILTER BY CITY
    # -------------------------
    filtered_data = filter_by_city(cleaned_data)

    print("Filtered records:", len(filtered_data))

    filtered_path = os.path.join(processed_dir, "national_trust_filtered.json")

    with open(filtered_path, "w") as f:
        json.dump(filtered_data, f, indent=2)

    print("Filtered data saved.")

    # -------------------------
    # STEP 6: VALIDATION
    # -------------------------
    validated_data = []
    rejected = 0

    for item in filtered_data:
        is_valid, error = validate_service(item)

        if is_valid:
            validated_data.append(item)
        else:
            rejected += 1
            print(f"REJECTED: {item.get('name')} -> {error}")

    print("Valid records:", len(validated_data))
    print("Rejected records:", rejected)

    validated_path = os.path.join(processed_dir, "national_trust_validated.json")

    with open(validated_path, "w") as f:
        json.dump(validated_data, f, indent=2)

    print("Validated data saved.")

    # -------------------------
    # STEP 7: REMOVE DUPLICATES
    # -------------------------
    deduped_data = remove_duplicates(validated_data)

    print("After duplicate removal:", len(deduped_data))

    final_path = os.path.join(processed_dir, "national_trust_final.json")

    with open(final_path, "w") as f:
        json.dump(deduped_data, f, indent=2)

    print("Final data saved.")

    # -------------------------
    # STEP 8: INSERT INTO DB
    # -------------------------
    insert_services(deduped_data)
    
    print("Data inserted into DB.")


if __name__ == "__main__":
    run_pipeline()