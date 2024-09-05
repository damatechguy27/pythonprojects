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

# https://www.tutorialspoint.com/python/tk_menu.htm

def command1():
    output = Label(root, text="you click File")
    output.pack()    

def command2():
    output = Label(root, text="you click on preference")
    output.pack()    


def command3():
    output = Label(root, text="you click For help")
    output.pack()    


#define menu 
mymenu = Menu(root)
root.config(menu=mymenu)

# create menu items

# this adds the file nmenu
file_menu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=command1)
file_menu.add_separator()
# root.quit exits the program  
file_menu.add_command(label="Exit", command=root.quit)

option_menu = Menu(mymenu)
mymenu.add_cascade(label="options", menu=option_menu)
option_menu.add_command(label="preferences", command=command2)
option_menu.add_separator()
option_menu.add_command(label="help", command=command3)



root.mainloop()

