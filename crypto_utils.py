import base64
from cryptography.fernet import Fernet

def get_fernet(key):
    return Fernet(base64.urlsafe_b64encode(key))

def encrypt(key, plaintext):
    return get_fernet(key).encrypt(plaintext.encode())

def decrypt(key, ciphertext):
    return get_fernet(key).decrypt(ciphertext).decode()
