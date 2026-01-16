import json
import os
from crypto_utils import hash_master_password, verify_master_password, generate_key, encrypt_data, decrypt_data
from getpass import getpass

VAULT_FILE = "vault.json"

def first_run_setup():
    print("Welcome! Let's get setup your Password Vault.")
    master_password = getpass('Enter your master password: ').strip()
    master_hash = hash_master_password(master_password)

    key = generate_key()
    encrypted_key = encrypt_data(master_hash.encode(), key.decode())

    data = {
        'master_password': master_hash,
        'key':encrypted_key,
        'vault':{}
    }
    with open('vault.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Setup complete! Your vault is ready")

def login():
    if not os.path.exists(VAULT_FILE):
        first_run_setup()
        return None, None

    with open(VAULT_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            print("Vault file is corrupted or empty. Recreating ")
            first_run_setup()
            return None, None

    for _ in range(3):
        master_password = getpass('master_password: ').strip()
        if verify_master_password(master_password, data['master_password']):
            key = decrypt_data(data['master_password'].encode(), data['key'])
            print("Login Successful!")
            return data, key
        else:
            print("Incorrect password. Try again.")
    print("Too many failed attempts. Exiting....")
    exit()

def add_credentials(data, key):
    service = input("Enter Service Name (eg: Gmail): ").strip()
    username = input("Enter Username/Email: ").strip()
    password = getpass("Enter Password: ").strip()

    encrypted_password = encrypt_data(key, password)

    data["vault"][service] = {
        "username": username,
        "password": encrypted_password
    }
    with open('vault.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Credentials for {service} added successfully!")

def view_credentials(data, key):
    service = input("Enter Service Name to View: ").strip()
    if service not in data["vault"]:
        print("Service does not exist. Try again.")
        return
    cred = data["vault"][service]
    decrypted_password = decrypt_data(key, cred["password"])
    print(f"\nService: {service}\nUsername: {cred['username']}\nPassword: {decrypted_password}\n")

def list_services(data):
    services = list(data["vault"].keys())
    if not services:
        print("No Credentials Stored Yet.")
        return
    print("Stored Services: ")
    for s in services:
        print(f"- {s}")
def main():
    data, key = login()
    while True:
        print("\n---- Password Vault ----")
        print("1. Add Credentials")
        print("2. View Credentials")
        print("3. List Credentials")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_credentials(data, key)
        elif choice == "2":
            view_credentials(data, key)
        elif choice == "3":
            list_services(data)
        elif choice == "4":
            print("\nGood Bye User.....\nExiting...")
            break
        else:
            print("Invalid Choice. Try again.")

if __name__ == "__main__":
    main()