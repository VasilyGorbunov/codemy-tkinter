from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')


def openwindow():
    global my_image
    top = Toplevel()
    top.title("Me Second Window")
    top.iconbitmap('1.ico')
    my_image = ImageTk.PhotoImage(Image.open("images/2.jpg"))
    Label(top, image=my_image).pack()
    Button(top, text="close window", command=top.destroy).pack()


Button(root, text="Open window", command=openwindow).pack()

root.mainloop()