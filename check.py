from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')
root.geometry("400x400")


def show():
    Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_label = Label(root, text=var.get());
my_label.pack()

Button(root, text="Show Selection", command=show).pack()

root.mainloop()
