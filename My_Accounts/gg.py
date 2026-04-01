import mysql.connector as msc
db = msc.connect(host = "localhost", username = "root",password = "root",database ="my_aacounts")
print("Connection Successful")
cursor = db.cursor()

sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
values = ("Pen", 50.00, 100)

cursor.execute(sql, values)
db.commit()

print("Data inserted!")