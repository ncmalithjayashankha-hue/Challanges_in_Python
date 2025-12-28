import sqlite3 as sql
# Connect to a database (or create it if it doesn't exist)
conn = sql.connect("students.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

conn.commit()
def add_student(name, marks):
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print(f"{name} added successfully!")
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
def update_marks(student_id, new_marks):
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))
    conn.commit()
    print(f"Student {student_id} marks updated!")
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student {student_id} deleted!")
while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Update marks")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)
    elif choice == "2":
        view_students()
    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        new_marks = int(input("Enter new marks: "))
        update_marks(student_id, new_marks)
    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
