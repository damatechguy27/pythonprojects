from tkinter import * 
from os.path import join
from PIL import Image, ImageTk
icon = join('resources','currency_dollar_icon.ico')
img = join('resources','moon.jpg')


#tkinter instance
root = Tk()

# add in icons 
root.iconbitmap(icon)

#add title to caption
root.title("Hello World")

#adding window size 
root.geometry("1280x720")

# user enter text 
enter_input = Entry(root,width=300, font="TimeRoman")
enter_input.pack()

label1 = ''


# button function what happens when you click
def click():
    global label1
    label1 = Label(root, text=enter_input.get())#.pack()
    label1.pack()


def show():
    label1.pack()


def hide():
    label1.pack_forget()

def destroy():
    label1.destroy()


#add images
image= ImageTk.PhotoImage(Image.open(img), size=(250,250))


imagelabel = Label(image=image)

#imagelabel.pack()

# creating the button and the click function
mybutton = Button(root,text="clickme", command=click)
mybutton.pack()

mybutton2 = Button(root,text="show", command=show)
mybutton2.pack()

mybutton3 = Button(root,text="hide", command=hide)
mybutton3.pack()

mybutton4 = Button(root,text="destroy", command=destroy)
mybutton4.pack()

root.mainloop()