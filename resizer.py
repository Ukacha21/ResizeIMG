from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("580x480")

global intx
global inty

intx = IntVar()

inty = IntVar()



heightLabel = Label(root, text="Height: ")
widthLabel = Label(root, text="Width: ")

heightget = Entry(root, textvariable=intx)
widthget = Entry(root, textvariable=inty)


#intx.set(150)
#inty.set(404)

#newheight = str(heightget)
#newwidth = str(widthget)

heightLabel.place(x=215, y=30)
widthLabel.place(x=215, y=60)

heightget.place(x=260, y=30)
widthget.place(x=260, y=60)

def browseFunc():

    global image
    image = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    
    imagetwo = Image.open(image)

    global next

    #resX = widthget.get()
    #resY = heightget.get()

    def it():

        if widthget.get() != ' ':
            global resX
            resX = int(widthget.get())
        if heightget.get() != ' ':
            global resY
            resY = int(heightget.get())

        global nextPic
        nextPic = imagetwo.resize((resX, resY), Image.ANTIALIAS)

    it()
    global resized

    resized = ImageTk.PhotoImage(nextPic)

    global imageLabel

    imageLabel = Label(root, image=resized)

    

def call():
    #del setOne
    #del setTwo
    print(image)

    intx.set(resX)
    inty.set(resY)
    #print(intx, inty)

    #print("found values for resX and resY are: ", resX, "/", resY)

    #imageLabel = browseFunc().imageLabel
    #imageLabel.pack()

    #here we need to save "0nextPic" wich is the resized picture
    #save = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    nextPic.save(filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]))


apply = Button(root, text="apply", command=call)
apply.pack(pady=100, padx=30)

browseButton = Button(root, text="Browse Picture", command=browseFunc)
browseButton.place(x=270, y=5)

mainloop()