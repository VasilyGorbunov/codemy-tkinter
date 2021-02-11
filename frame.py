from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')

frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click there")
b2 = Button(frame, text="... or here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()