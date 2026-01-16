import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="test_python")
    mycursor = conn.cursor()
    sql = "select * from students where Stu_name='%s'"
    mycursor.execute(sql)
    for row in mycursor:
        print(row)

    print("Connected to MySQL")

    # while True:
    #     print("menu")
    #     choice = input("Enter your choice: ")

except mysql.connector.Error as e:
    print("Connection Error: ",e)