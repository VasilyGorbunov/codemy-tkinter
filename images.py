from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')

my_img = ImageTk.PhotoImage(Image.open('1.jpg'))
my_label = Label(image=my_img, height=500)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()