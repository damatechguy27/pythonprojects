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

v = IntVar()

def radio():
    if v.get() == 1:
        mylabel = Label(root, text="stop clicking me")
    else:
        mylabel = Label(root, text="I am warning you!")
    #mylabel = Label(root, text=v.get())
    mylabel.pack()


rbutton1 = Radiobutton(root, text="One", variable=v, value=1).pack()

rbutton2 = Radiobutton(root, text="Two", variable=v, value=2).pack()

mybutton = Button(root, text="submit", command=radio).pack()
root.mainloop()