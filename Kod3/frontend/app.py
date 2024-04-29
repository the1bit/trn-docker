from flask import Flask, request, jsonify, json
import random
import mysql.connector
from mysql.connector import Error
import os
import random

app = Flask(__name__)


def generate_random_hungarian_sentence():
    subjects = ["A kutya", "A macska", "Az ember", "A gomba", "A moszat"]
    verbs = ["ugrik", "fut", "eszik", "olvas", "vezet", "iszik"]
    objects = ["vizet", "botot", "kenyeret", "cikket", "brokkolit", "tejet"]
    adjectives = ["gyors", "nagy", "piros", "izgalmas", "finom", "hideg"]

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    adjective = random.choice(adjectives)

    # Egyszerű mondatszerkezet: Tárgy + Ige + Melléknév + Tárgy
    sentence = f"{subject} {verb} egy {adjective} {obj}"
    return sentence


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
    )
    return connection


@app.route("/ujadatbazis")
def new_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        db_name = os.getenv("DB_NAME")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        # Select the database
        conn.database = db_name

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY, adat VARCHAR(255))"
        )
        conn.commit()

        return "Adatbázis és tábla létrehozva."
    except Error as e:
        return f"An error occurred: {e}"

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


@app.route("/ujelem")
def add_data():

    number = int(request.args.get("elemszam", 10))
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(number):
        item = generate_random_hungarian_sentence()
        query = "INSERT INTO items (adat) VALUES (%s)"
        cursor.execute(query, (item,))
    conn.commit()
    conn.close()
    return f"Hozzáadott elemek száma: {number}"


@app.route("/adatok")
def list_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT adat FROM items")
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)


@app.route("/torol")
def delete_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items")
    conn.commit()
    conn.close()
    return "Minden adat törölve."


@app.route("/")
def home():
    return jsonify(
        {
            "leiras": "Python + MariaDB + Docker",
            "vegpontok": {
                "/ujadatbazis": "Új adatbázis létrehozása",
                "/ujelem?elemszam=10": "Új elemek hozzáadása",
                "/adatok": "Elemek listázása",
                "/torol": "Minden elem törlése",
            },
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
