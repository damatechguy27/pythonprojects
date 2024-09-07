from tkinter import * 
from os.path import join
from PIL import Image, ImageTk
icon = join('resources','currency_dollar_icon.ico')
img = join('resources','moon.jpg')

#tkinter instance
root = Tk()

# add in icons 
#root.iconbitmap(icon)

#add title to caption
root.title("Hello World")

#adding window size 
root.geometry("1280x720")

v = StringVar()

def radio():
    if v.get() == "cheese":
        mylabel = Label(root, text="stop clicking me")
    elif v.get() == "no cheese":
        mylabel = Label(root, text="I am warning you!")
    #mylabel = Label(root, text=v.get())
    mylabel.pack()


checkbutton1 = Checkbutton(root, text="One", variable=v, onvalue="cheese", offvalue="no cheese")

#checkbutton2 = Checkbutton(root, text="two", variable=v, onvalue="ice", offvalue="no ice")

checkbutton1.deselect()

#checkbutton2.deselect()

checkbutton1.pack()
#checkbutton2.pack()

mybutton = Button(root, text="submit", command=radio).pack()
root.mainloop()