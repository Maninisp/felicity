from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Allow frontend origins (adjust later for production)
CORS(app)

# ---------------------------------------
# Database Connection (Using .env file)
# ---------------------------------------
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


# ---------------------------------------
# Health Check
# ---------------------------------------
@app.route("/")
def home():
    return "Felicity Backend Running"


# ---------------------------------------
# GET Services (with filters)
# ---------------------------------------
@app.route("/services", methods=["GET"])
def get_services():

    page = request.args.get("page")
    city = request.args.get("city")
    condition = request.args.get("condition")
    type_filter = request.args.get("type")

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
        SELECT DISTINCT s.id, s.name, s.page, s.type, s.city
        FROM services s
        LEFT JOIN service_conditions sc ON s.id = sc.service_id
        LEFT JOIN conditions c ON sc.condition_id = c.id
        WHERE 1=1
    """

    params = []

    if page:
        query += " AND s.page = %s"
        params.append(page)

    if city:
        query += " AND s.city = %s"
        params.append(city)

    if condition:
        query += " AND c.slug = %s"
        params.append(condition)

    if type_filter:
        query += " AND s.type = %s"
        params.append(type_filter)

    cur.execute(query, params)
    rows = cur.fetchall()

    services = [
        {
            "id": row[0],
            "name": row[1],
            "page": row[2],
            "type": row[3],
            "city": row[4]
        }
        for row in rows
    ]

    cur.close()
    conn.close()

    return jsonify(services)


# ---------------------------------------
# POST - Add Service
# ---------------------------------------
@app.route("/services", methods=["POST"])
def add_service():
    data = request.get_json()

    required_fields = ["name", "page", "type", "city"]

    for field in required_fields:
        if field not in data or not data[field]:
            return {"error": f"{field} is required"}, 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO services (name, page, type, description, address, city, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data["name"],
            data["page"],
            data["type"],
            data.get("description"),
            data.get("address"),
            data["city"],
            data.get("phone")
        ))

        new_id = cur.fetchone()[0]
        conn.commit()

    except Exception:
        conn.rollback()
        cur.close()
        conn.close()
        return {"error": "Duplicate service exists"}, 400

    cur.close()
    conn.close()

    return {
        "message": "Service added successfully",
        "id": new_id
    }, 201


# ---------------------------------------
# PUT - Update Service
# ---------------------------------------
@app.route("/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE services
        SET name=%s, page=%s, type=%s, description=%s, address=%s, city=%s, phone=%s
        WHERE id=%s
        RETURNING id
    """, (
        data["name"],
        data["page"],
        data["type"],
        data.get("description"),
        data.get("address"),
        data["city"],
        data.get("phone"),
        service_id
    ))

    updated = cur.fetchone()

    if not updated:
        cur.close()
        conn.close()
        return {"error": "Service not found"}, 404

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Service updated successfully"}


# ---------------------------------------
# DELETE - Remove Service
# ---------------------------------------
@app.route("/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM services WHERE id = %s RETURNING id", (service_id,))
    deleted = cur.fetchone()

    if not deleted:
        cur.close()
        conn.close()
        return {"error": "Service not found"}, 404

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Service deleted successfully"}


# ---------------------------------------
# Run App
# ---------------------------------------
if __name__ == "__main__":
    app.run(debug=True)