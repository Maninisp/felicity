# backend/pipeline/core/inserter.py

from db import get_connection


def insert_service(service):
    """
    Inserts a validated service into PostgreSQL.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO services (name, city, category)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (
        service["name"],
        service["city"],
        service["category"]
    ))

    conn.commit()

    cursor.close()
    conn.close()