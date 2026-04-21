import mysql.connector
from config.config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        skills TEXT,
        experience FLOAT,
        education TEXT,
        resume_text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()