from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')

def popup():
    response = messagebox.askyesno("This is my popup!", "Hello world!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked YES!").pack()
    else:
        Label(root, text="You clicked NO!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()