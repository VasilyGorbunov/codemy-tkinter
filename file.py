from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Python')
root.iconbitmap('1.ico')

root.filename = filedialog.askopenfilename(
    initialdir="images",
    title="Select A File",
    filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg"))
)
Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
Label(root, image=my_image, height=400).pack()

def openimage():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="images",
        title="Select A File",
        filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg"))
    )
    Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=my_image, height=400).pack()

Button(root, text="Open image", command=openimage).pack()

root.mainloop()