final_marks = []

def add_mark():
    marks = input("Enter the Marks to Add (0-100): ").strip()
    if marks.isdigit():
        marks = int(marks)
        if 0 <= marks <= 100:
            final_marks.append(marks)
            print(f"Mark {marks} added successfully")
        else:
            print("Please enter a number between 0 and 100")
    else:
        print("Invalid input, enter a number")

def show_stats():
    if not final_marks:
        print("No marks to show")
        return
    total = sum(final_marks)
    average = total / len(final_marks)
    print(f"""
Total Marks  : {total}
Average Marks: {average:.2f}
Highest Marks: {max(final_marks)}
Lowest Marks : {min(final_marks)}
Number of Students: {len(final_marks)}
""")

def remove_mark():
    if not final_marks:
        print("No marks to remove")
        return
    print("Marks:", ", ".join(f"{i}:{m}" for i, m in enumerate(final_marks)))
    idx = input("Enter the index of the mark to remove: ").strip()
    if idx.isdigit():
        idx = int(idx)
        if 0 <= idx < len(final_marks):
            removed = final_marks.pop(idx)
            print(f"Mark {removed} removed successfully")
        else:
            print("Index out of range")
    else:
        print("Invalid input")

# Menu Loop
while True:
    print("""
==== Menu ====
1. Add a New Mark
2. Show All Marks
3. Show Statistics
4. Remove a Mark
5. Exit
""")
    option = input("Enter your choice: ").strip()
    if option.isdigit():
        option = int(option)
        if option == 1:
            add_mark()
        elif option == 2:
            print("All Marks:", ", ".join(map(str, final_marks)) if final_marks else "No marks added")
        elif option == 3:
            show_stats()
        elif option == 4:
            remove_mark()
        elif option == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")
    else:
        print("Invalid input, enter a number 1-5")
