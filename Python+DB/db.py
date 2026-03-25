import mysql.connector
from tabulate import tabulate as t
conn = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
c = conn.cursor()

def custom_query():
    while True:
        query = input("query(0 to exit) #").strip()
        if query == "0" or query == "exit" or query == "" or query == "q":
            break
        else:
            c.execute(query)
def insert_data():
    c.execute('select * from caption')
    print(t(c.fetchall(), headers=["ID", "Name", "Address", "DoB", "Loyalty Points"], tablefmt="fancy_grid"))
    while True:
        d = input("Do you want to Customize this Query(Y/n)").strip().lower()
        if d == "y" or d == "":
            custom_query()
def update_data():
    print()
def delete_data():
    print()
def show_data():
    c.execute('select * from caption')
    print(t(c.fetchall(), headers=["ID", "Name", "Address", "DoB", "Loyalty Points"], tablefmt="fancy_grid"))
    while True:
        d = input("Do you want to Customize this Query(Y/n)").strip().lower()
        if d == "y" or d == "":
            custom_query()
def select_oprt():
    while True:
        print('''
        Possible Operations:
        
        1. Insert data
        2. Update data
        3. Delete data
        4. View data
        5. Exit''')
        c = input("Enter the Choice").lower().strip()
        if c not in ['1','2','3','4','5']:
            print("Invalid Choice")
            continue
        elif c == '1':
            insert_data()
        elif c == '2':
            update_data()
        elif c == '3':
            delete_data()
        elif c == '4':
            show_data()
        else:
            print("Thank you for choosing us")
            break


c.execute('select * from caption')
print(t(c.fetchall(),headers=["ID","Name","Address","DoB","Loyalty Points"],tablefmt="fancy_grid"))
select_oprt()
conn.close()