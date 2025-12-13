students = {}

try:
    with open("students.txt", "r") as f:
        for line in f:
            name, sci, math, ict, avg = line.strip().split(",")
            students[name] = {
                "Science": int(sci),
                "Math": int(math),
                "ICT": int(ict),
                "Average": float(avg)
            }
except FileNotFoundError:
    pass   # file doesn't exist on first run, so ignore

while True:
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ")
        science = int(input("Science marks: "))
        math = int(input("Math marks: "))
        ict = int(input("ICT marks: "))

        average = (science + math + ict) / 3

        students[name] = {
            "Science": science,
            "Math": math,
            "ICT": ict,
            "Average": average
        }

        print("\nStudent added successfully!")


    elif choice == "2":
        if not students:
            print("\nNo students added yet!")
        else:
            print("\n" + "_" * 80)
            print(f"| {'Name':15} | {'Science':10} | {'Math':10} | {'ICT':10} | {'Average':10} |")
            print("-" * 80)

            for name, data in students.items():
                print(
                    f"| {name:15} | {data['Science']:10} | {data['Math']:10} | {data['ICT']:10} | {data['Average']:10.2f} |")


    elif choice == "3":
        search_name = input("Enter the student name to search: ")

        if search_name in students:
            data = students[search_name]
            print("\nStudent Found!")
            print("-" * 40)
            print(f"Name     : {search_name}")
            print(f"Science  : {data['Science']}")
            print(f"Math     : {data['Math']}")
            print(f"ICT      : {data['ICT']}")
            print(f"Average  : {data['Average']:.2f}")
        else:
            print("\nStudent not found!")


    elif choice == "4":
        remove_name = input("Enter the student name to remove: ")

        if remove_name in students:
            del students[remove_name]
            print(f"{remove_name} has been removed successfully!")
        else:
            print("Student not found!")


    elif choice == "5":
        with open("students.txt", "w") as f:
            for name, data in students.items():
                line = f"{name},{data['Science']},{data['Math']},{data['ICT']},{data['Average']}\n"
                f.write(line)

        print("All data saved! Exiting...")

        break

    else:
        print("Invalid option, try again!")
