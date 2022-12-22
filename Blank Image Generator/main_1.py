from tkinter import *

from tkinter import colorchooser, filedialog

from PIL import Image


def choose_colour():
    color_code = colorchooser.askcolor()
    colorEntryBox.delete(0, END)
    colorEntryBox.insert(END, "{},{},{}".format(int(color_code[0][0]), int(color_code[0][1]), int(color_code[0][2])))


def createimage():
    color = colorEntryBox.get()
    extension = extensionEntryBox.get()
    width = int(widthEntryBox.get())
    height = int(heightEntryBox.get())
    images = imagesEntryBox.get()
    name = nameEntryBox.get()
    url = filedialog.askdirectory()
    convertStatusLabel.configure(text="{} - Creating Images------".format(images))

    col = color.split(',')
    colorname = []
    try:
        for i in col:
            colorname.append(int(i))
        colorname = tuple(colorname)
    except:
        colorname = col[0]
    for i in range(int(images)):
        path = url + "/{}{}{}".format(name, i+1, extension)
        im = Image.new("RGB", (width, height), color=colorname)
        im.save(path)
    convertStatusLabel.configure(text="{} - Creating Images successfully".format(images))


root = Tk()

root.title("Image Generator")
root.iconbitmap("./logo.ico")
root.geometry("712x508+300+100")
root.resizable("false", "false")
root.configure(bg="sky blue")

# --------------labels-----------------
colorLabel = Label(root, text="Colour", font=("arial", 20, "bold"), bg="sky blue")
colorLabel.place(x=50, y=10)

extensionLabel = Label(root, text="Extension", font=("arial", 20, "bold"), bg="sky blue")
extensionLabel.place(x=50, y=80)

widthLabel = Label(root, text="Width", font=("arial", 20, "bold"), bg="sky blue")
widthLabel.place(x=50, y=150)

heightLabel = Label(root, text="Height", font=("arial", 20, "bold"), bg="sky blue")
heightLabel.place(x=50, y=220)

imagesLabel = Label(root, text="Images No", font=("arial", 20, "bold"), bg="sky blue")
imagesLabel.place(x=50, y=290)

nameLabel = Label(root, text="Name", font=("arial", 20, "bold"), bg="sky blue")
nameLabel.place(x=50, y=370)

convertStatusLabel = Label(root, text=" ", font=("arial", 18, "bold"), bg="sky blue", width=38)
convertStatusLabel.place(x=50, y=468)


# --------------Entry boxes-------------
colorEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                      fg="black", selectbackground="white", selectforeground="red")
colorEntryBox.insert(END, "255,255,255")
colorEntryBox.place(x=230, y=10, height=45, width=350)

extensionEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                          fg="black", selectbackground="white", selectforeground="red")
extensionEntryBox.insert(END, ".png")
extensionEntryBox.place(x=230, y=80, height=45, width=460)

widthEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                      fg="black", selectbackground="white", selectforeground="red")
widthEntryBox.insert(END, "800")
widthEntryBox.place(x=230, y=150, height=45, width=460)

heightEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                       fg="black", selectbackground="white", selectforeground="red")
heightEntryBox.insert(END, "800")
heightEntryBox.place(x=230, y=220, height=45, width=460)

imagesEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                       fg="black", selectbackground="white", selectforeground="red")
imagesEntryBox.insert(END, "5")
imagesEntryBox.place(x=230, y=290, height=45, width=460)

nameEntryBox = Entry(root, font=("arial", 14, "italic bold"), bg="yellow", bd=5, justify="center", relief="sunken",
                     fg="black", selectbackground="white", selectforeground="red")
nameEntryBox.insert(END, "RedImages")
nameEntryBox.place(x=230, y=360, height=45, width=460)


# --------------buttons-----------------

button = Button(root, text="select colour", font=("arial", 10, "bold"), bg="red", bd=5, justify="center",
                relief="ridge", fg="black", activebackground="blue", activeforeground="white", command=choose_colour)
button.place(x=590, y=10, height=45, width=100)

createSingleBtn = Button(root, text="Create Coloured Images", font=("arial", 15, "bold"), bg="red", bd=5,
                         justify="center", relief="ridge", fg="black", activebackground="blue",
                         activeforeground="white", width=53, command=createimage)
createSingleBtn.place(x=50, y=420, height=45,)


root.mainloop()
