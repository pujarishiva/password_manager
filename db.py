import sqlite3

DB_NAME = "vault.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS master (
        id INTEGER PRIMARY KEY,
        password_hash BLOB,
        salt BLOB
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS vault (
        service TEXT PRIMARY KEY,
        username TEXT,
        password BLOB
    )
    """)

    conn.commit()
    conn.close()
