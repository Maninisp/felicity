# pipeline/db/insert_services.py

from db import get_connection


def insert_services(services):

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO services (
        name, category, city, state,
        address, email, phone,
        service_type, conditions
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for s in services:
        cur.execute(query, (
            s.get("name"),
            s.get("category"),
            s.get("city"),
            s.get("state"),
            s.get("address"),
            s.get("email"),
            s.get("phone"),
            s.get("service_type"),
            s.get("conditions")
        ))

    conn.commit()
    cur.close()
    conn.close()