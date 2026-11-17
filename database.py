
import sqlite3
from security import hash_password, verify_password

DB_NAME = "users.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = connect()

    try:
        hashed_password = hash_password(password)

        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def login_user(username, password):
    conn = connect()

    try:
        cursor = conn.execute(
            "SELECT password FROM users WHERE username = ?",
            (username,)
        )

        result = cursor.fetchone()

        if result and verify_password(password, result[0]):
            return True

        return False

    finally:
        conn.close()
