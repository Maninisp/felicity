# backend/db.py

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Creates and returns a PostgreSQL connection.
    Used by both Flask app and pipeline.
    """

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return conn