import hashlib
from core.database import get_connection
from core.logger import get_logger

logger = get_logger("AUTH")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "SELECT id,username, role FROM users WHERE username = ? AND password = ?",
        (username, hashed)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        logger.info(f"User logged in: {username}")
    else:
        logger.warning(f"Failed login attempt: {username}")

    return user