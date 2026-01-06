import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from db import get_connection

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000
    )
    return kdf.derive(password.encode())

def setup_master_password(password):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO master (password_hash, salt) VALUES (?, ?)",
        (key, salt)
    )
    conn.commit()
    conn.close()

def verify_master_password(password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_hash, salt FROM master LIMIT 1")
    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    stored_hash, salt = row
    key = derive_key(password, salt)

    if key == stored_hash:
        return key
    return None
