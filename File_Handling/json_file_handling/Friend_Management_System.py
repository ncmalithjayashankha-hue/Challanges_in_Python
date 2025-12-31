import json

db_file = "friends.json"

try:
    with open(db_file, "a") as update_file:
        def lets_update(a):
            json.dump(a, update_file)

    with open(db_file , "r+") as read_file:
        dicti = json.load(read_file)
        def view():
            print("Current Friends:\n")
            print("|Name   |   Age  |Status | Skills|")
            for friend in dicti:
                print(f"{friend["Name"]:8} - {friend["Age"]:3} - {friend["Active"]:5} - {friend["Skills"]}")
        def add():
            print("---- Add a New Friend ----")
            name = input("Enter a friend's name: ").strip()

            if not name.lower() in dicti:
                age = int(input("Enter a friend's age: ").strip())
                active = int(input("Enter a friend's active status: ").strip())
                skills = input("Enter a friend's skills (Separated by commas): ").strip().split(",")
            else:
                print("Friend Already Exists")
            new_dict = {"Name": name, "Age": age, "Skills": skills, "Active": active}

            json.dump(new_dict, read_file)
            print("New Friend Added Successfully")
        def update():
            print("---- Update Friend Details ----")
            while True:
                print("____ Details to Update Friend Details ____")
                print("""
                1. Name
                2. Age
                3. Skills
                4. Active
                5. Exit
                """)
                input_choice = input("Enter your choice: ").strip()
                if input_choice == "1":
                    name = input("Enter a friend's name: ").strip()
                elif input_choice == "2":
                    age = int(input("Enter a friend's age: ").strip())
                elif input_choice == "3":
                    skills = input("Enter a friend's skills: ").strip().split(",")
                elif input_choice == "4":
                    active = bool(input("Enter a friend's active status: ").strip())
                elif input_choice == "5":
                    break
                else:
                    print("Invalid Choice (try a number between 1 and 6): ")
            update_dict = {"Name": name, "Age": age, "Skills": skills, "Active": active}
            lets_update(update_dict)
            print("Friend Details Updated Successfully")
        def delete():
            pass
        def search():
            pass
        def main():
            while True:
                print(f"==== Friend Management System ====\n"
                      f"\n"
                      f"1. View All Friends.\n"
                      f"2. Add a new friend.\n"
                      f"3. Update Friend Details.\n"
                      f"4. Delete a Friend.\n"
                      f"5. Search friends by skill.\n"
                      f"6. Exit\n")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    view()
                elif choice == "2":
                    add()
                elif choice == "3":
                    update()
                elif choice == "4":
                    delete()
                elif choice == "5":
                    search()
                elif choice == "6":
                    print("Thank you for using Friend Management System")
                    exit()
                else:
                    print("Invalid Choice (try a number between 1 and 6).)")
        main()
except NameError:
    print("Name Error")
except KeyboardInterrupt:
    print("\nThank you for using Friend Management System")
except FileNotFoundError:
    print("File Not Found")
except TypeError:
    print("Type Error")
# except json.JSONDecodeError:
#     print("JSON Error")