import csv
access = False
def verify():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'admin' and password == 'Admin123':
        access = True
    else:
        return False

def add():
    if access:
        with open('students.csv','a',newline="") as f:
            nm = input('Enter your name: ')
            name = '\n'+nm
            f.write(name)

    else:
        print("You don't have permission to do that.")


def menu():
    while True:
        print("""
        ==== Menu ====
        1. Add Student
        2. View Students
        3. Search Students
        4. Update Students
        5. Delete Students
        6. Generate Report
        7. Exit
        """)
        choice = input(">>>")
