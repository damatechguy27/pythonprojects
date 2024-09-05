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

#add images
image= ImageTk.PhotoImage(Image.open(img))

imagelabel = Label(root,image=image)

imagelabel.pack()

root.mainloop()

