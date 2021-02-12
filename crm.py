from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')
root.geometry("400x400")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="codemy",
)

my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE codemy")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# my_cursor.execute("""CREATE TABLE customers (
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     zipcode INT(10),
#     price_paid DECIMAL(10, 2),
#     user_id INT AUTO_INCREMENT PRIMARY KEY
# )""")

my_cursor.execute("SELECT * FROM customers")
for thing in my_cursor.description:
    print(thing)

root.mainloop()
