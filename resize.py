from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("480x480")
root['bg'] = 'turquoise'

pic = Image.open('screen.png')

resized = pic.resize((280, 200), Image.ANTIALIAS)

newPic = ImageTk.PhotoImage(resized)

label = Label(root, image=newPic)
label.pack(pady=20)



mainloop()