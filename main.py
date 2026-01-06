from getpass import getpass
from db import init_db, get_connection
from auth import setup_master_password, verify_master_password
from crypto_utils import encrypt, decrypt
from password_utils import generate_password, is_strong

def main():
    init_db()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM master")
    exists = cur.fetchone()[0]
    conn.close()

    if exists == 0:
        print("🔐 Setup Master Password")
        master = getpass("Create Master Password: ")
        setup_master_password(master)
        print("✅ Master password set\n")

    print("🔑 Login")
    master = getpass("Enter Master Password: ")
    key = verify_master_password(master)

    if not key:
        print("❌ Wrong master password")
        return

    print("✅ Access granted")

    while True:
        print("\n1. Add Password")
        print("2. View Password")
        print("3. Generate Strong Password")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            service = input("Service: ")
            username = input("Username: ")

            pwd = getpass("Password (leave empty to generate): ")
            if not pwd:
                pwd = generate_password()
                print("Generated Password:", pwd)

            if not is_strong(pwd):
                print("⚠ Weak password detected")

            encrypted = encrypt(key, pwd)

            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "REPLACE INTO vault VALUES (?, ?, ?)",
                (service, username, encrypted)
            )
            conn.commit()
            conn.close()

            print("✅ Stored securely")

        elif choice == "2":
            service = input("Service: ")

            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT username, password FROM vault WHERE service=?",
                (service,)
            )
            row = cur.fetchone()
            conn.close()

            if not row:
                print("❌ Not found")
            else:
                username, encrypted = row
                print("Username:", username)
                print("Password:", decrypt(key, encrypted))

        elif choice == "3":
            print("Strong Password:", generate_password())

        elif choice == "4":
            print("🔒 Auto-locked")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
