import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="test_python")
c = conn.cursor()
print("Connected to MySQL")


def add():
    name=input("Please enter your name: ").strip()
    get_dob = input("Please enter your birth date: ").strip().replace(" ","").split("/")
    dob = f"{get_dob[0]}-{get_dob[1]}-{get_dob[2]}"
    email = input("Please enter your email address: ").strip()
    c.execute("insert into students (Stu_name,DOB,Email) values(%s,%s,%s)",(name,dob,email))
    conn.commit()
    print("Student added")

def view_all():
    c.execute("select * from students")
    students = c.fetchall()
    for student in students:
        print(student)



def main_menu():
    while True:
        print("==== LMS ====\n"
              "1.Add Student\n"
              "2.View Student Details\n"
              "3.View All Details\n"
              "4.Delete Student Details\n"
              "5.Update Student Details\n"
              "6.Exit\n")
        option = input("Please enter your choice: ").strip()
        if option == "1":
            add()
        elif option == "2":
            pass
        elif option == "3":
            view_all()
        elif option == ("6"):
            break
        else:
            print("Invalid option")





main_menu()