import mysql.connector
from tabulate import tabulate as t
conn = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
c = conn.cursor()

def insert_data():
    print()
def update_data():
    print()
def delete_data():
    print()
def show_data():
    print()
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
conn.close()