students = {}

def add_student():
    number = f"S{len(students) + 1:03}"
    name = input("Enter your name: ")

    # --- Get Maths marks ---
    mm = int(input("Enter Maths marks (0-100): "))
    while mm < 0 or mm > 100:
        print("Invalid! Enter between 0 - 100")
        mm = int(input("Enter Maths marks (0-100): "))

    # --- Get Science marks ---
    ms = int(input("Enter Science marks (0-100): "))
    while ms < 0 or ms > 100:
        print("Invalid! Enter between 0 - 100")
        ms = int(input("Enter Science marks (0-100): "))

    # --- Get English marks ---
    me = int(input("Enter English marks (0-100): "))
    while me < 0 or me > 100:
        print("Invalid! Enter between 0 - 100")
        me = int(input("Enter English marks (0-100): "))

    # --- Save student data ---
    students[number] = {
        "ID": number,
        "Student": name,
        "Math": mm,
        "Science": ms,
        "English": me
    }

    print("New Student Added Successfully!")
