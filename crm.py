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
    passwd="root"
)

print(mydb)

root.mainloop()
