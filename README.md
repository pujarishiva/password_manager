# 🔐Secure Password Manager

**secure CLI-based password manager** built using Python, designed to safely store and manage credentials using industry-standard encryption and authentication practices.

---

## 🛡 Features

- **Master Password Authentication**: Secure login using a master password (hashed + salted, never stored in plaintext)
- **AES Encryption**: All stored passwords are encrypted at rest using symmetric AES encryption (Fernet)
- **Secure Key Derivation**: PBKDF2-HMAC-SHA256 ensures brute-force resistance
- **SQLite Database Storage**: Credentials stored securely in an encrypted-friendly database
- **Add / View / Generate Passwords**: Add, retrieve, and generate strong passwords
- **Password Strength Validation**: Warns against weak passwords according to OWASP rules
- **Auto-Lock Concept**: CLI can exit to protect against unauthorized access

---

## 🧠 Security Highlights

- **PBKDF2 key derivation** with 200,000 iterations  
- **AES-256 encryption** for password storage  
- **Salted password hashes** for master password  
- **No plaintext passwords stored anywhere**  
- **Secure password generation** (letters, digits, symbols)  

---

## 🛠 Tech Stack

- Python 3.10+  
- [cryptography](https://cryptography.io/en/latest/) library  
- SQLite (local database)  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/advanced-password-manager.git
cd advanced-password-manager

##Run the application
-python main.py