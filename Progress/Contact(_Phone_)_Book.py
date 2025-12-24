contacts = {}

def get_valid_phone():
    while True:
        phone = input("Enter Phone number(10 Digits , starts with 0)")
        if phone.isdigit() and len(phone) == 10 and phone.startswith ("0"):
            return phone
        print("Invalid phone.try again")

def add_contact():
    name = input("Enter the name to Add: ").strip()
    if not name:
        print("Name cannot be Empty:")
        return
    phone = get_valid_phone()
    key = f"T{len(contacts) + 1:03}"
    contacts[key] = {"Name": name, "Phone": phone}
    print(f"Added: {name} - {phone}")
    print(contacts)

def search_contacts():
    name = input("Enter the name to Search: ").strip().lower()
    found = False
    for key, data in contacts.items():
        if data["Name"].lower() == name:
            print(f"{key} - {data['Name']} - {data['Phone']}")
            found = True
        if not found:
            print("Contact not found !")

def delete_contact():
    key = input("Enter the key to Delete: ").strip().title()
    if key in contacts:
        del contacts[key]
        print(f"{key} Deleted")
    else:
        print("Contact not found !")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print("\n==== Contact List ====")
    for key, data in sorted(contacts.items()):
        print(f"{data["Name"]} - {data["Phone"]}")
    print("======================")

def main_menu():
    while True:
        print("""
        \n==== Contact Book ====
        1. Add Contact
        2. Search Contact
        3. View All Contacts
        4. Delete Contact
        5. Exit
        """)
        choice = int(input("Choose option (1 - 5): "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contacts()
        elif choice == 3:
            view_contacts()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Good Bye User...! ")
            break
        else:
            print("Invalid option. Enter 1 - 5")

if __name__ == "__main__":
    main_menu()