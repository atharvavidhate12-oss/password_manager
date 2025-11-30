import json
import bcrypt
from cryptography.fernet import Fernet
import os

VAULT_KEY_FILE = "vault.key"
CREDENTIALS_FILE = "credentials.json"

# Generate or load key
def load_key():
    if not os.path.exists(VAULT_KEY_FILE) or os.path.getsize(VAULT_KEY_FILE) == 0:
        key = Fernet.generate_key()
        with open(VAULT_KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(VAULT_KEY_FILE, "rb") as f:
            key = f.read()
        # Validate key - if invalid, regenerate it
        try:
            Fernet(key)  # Test if key is valid
        except ValueError:
            # Key is invalid, regenerate it
            key = Fernet.generate_key()
            with open(VAULT_KEY_FILE, "wb") as f:
                f.write(key)
    return Fernet(key)

# Save encrypted credentials
def save_credentials(site, username, password):
    fernet = load_key()

    entry = {
        "site": site,
        "username": fernet.encrypt(username.encode()).decode(),
        "password": fernet.encrypt(password.encode()).decode()
    }

    data = []
    if os.path.exists(CREDENTIALS_FILE) and os.path.getsize(CREDENTIALS_FILE) > 0:
        try:
            with open(CREDENTIALS_FILE, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            # File exists but is corrupted, start fresh
            data = []

    data.append(entry)
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Read stored credentials
def view_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        print("No credentials stored yet.")
        return

    fernet = load_key()
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, ValueError):
        print("Error: Credentials file is corrupted. No credentials can be displayed.")
        return

    for entry in data:
        print("\n Site:", entry["site"])
        print(" Username:", fernet.decrypt(entry["username"].encode()).decode())
        print("Password:", fernet.decrypt(entry["password"].encode()).decode())
