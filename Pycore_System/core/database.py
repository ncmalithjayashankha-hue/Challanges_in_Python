import sqlite3
import os
from core.logger import get_logger

logger = get_logger("DATABASE")

DB_PATH = "data/app.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized")
def add_user(username,password,role='user'):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        logger.info(f"User {username} added")
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def list_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, role FROM users")
    users = cursor.fetchall()

    conn.close()
    return users