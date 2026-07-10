import hashlib as h
def encrypt_password(password):
    return h.md5(password.encode()).hexdigest()

def addnew():
    account = input("Enter the Site / Account Name").strip().lower()
    username = input("Enter the Username").strip()
    password = input("Enter the Password").strip()

    with open('pwd.txt','a') as f:
        f.write(f"{account},{encrypt_password(username)},{encrypt_password(password)}\n")

def view():
    with open('pwd.txt','r') as f:
        for line in f:
            ele = line.strip().split(',')
            print(f"Account Name: {ele[0]}\n\tUsername: {ele[1]} \n")

def search_p():
    with open('pwd.txt','r') as f:
        acc_no = input('Enter the Account Name').strip()
        for line in f:
            element = line.strip().split(',')
            if element[0] == acc_no.lower():
                print(f"Account Name: {element[0].title()}\n\tUsername: {element[1]} \n\tPassword: {element[2]}")

def del_p():
    rewrite = []
    found = False
    with open('pwd.txt','r') as f:
        acc_no = input('Enter the Account Name').strip()
        for line in f:
            element = line.strip().split(',')
            if element[0] == acc_no.lower():
                found = True
                continue
            else:
                rewrite.append(line)
    with open(f"pwd.txt","w") as f2:
        for line in rewrite:
            f2.write(line)
    if found:
        print("Account Deleted Successfully")
    else:
        print("Account Not Found")


def menu():
    while True:
        print(f"{'='*4} PASSWORD VAULT {'='*4}")
        print('1. Add Password \n2. View Saved Accounts \n3. Search Account \n4. Delete Account \n5. Exit')
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            addnew()
        elif choice == '2':
            view()
        elif choice == '3':
            search_p()
        elif choice == '4':
            del_p()
        elif choice == '5':
            print("Thank you for using Password Vault")
            break
        else:
            print("Invalid Choice")
            continue
def auth():
    menu()
auth()