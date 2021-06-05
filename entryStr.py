from tkinter import *

root = Tk()
root.geometry("480x480")

#v = StringVar()

entry = Entry(root)
entry.pack()

global s

#s = v.get()


#v.set(s)


def apply():
    #v.set()
    s = entry.get()
    label = Label(root, text=s)
    label.pack()

button = Button(root, text="Show", command=apply)
button.pack()

mainloop()

