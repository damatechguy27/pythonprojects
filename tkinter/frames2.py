#menus and frames
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


def command1():
    #output = Label(root, text="you click File")
    #output.pack() 
    hideframe() 
    theframe.grid(row=2,column=0,columnspan=4,rowspan=4,padx=10,pady=10)  

def command2():
    #output = Label(root, text="you click on preference")
    #output.pack()
    hideframe() 
    theframe2.grid(row=2,column=0,columnspan=4,rowspan=4,padx=10,pady=10)   


def command3():
    output = Label(root, text="you click For help")
    output.pack()    


def hideframe():
    theframe.grid_forget()
    theframe2.grid_forget()

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


# The Frame
theframe = Frame(root,width=200,height=200,bd=7,bg='red')
#theframe.grid(row=2,column=0,columnspan=4,rowspan=4,padx=10,pady=10)


theframe2 = Frame(root,width=200,height=200,bd=7,bg='blue')
#theframe2.grid(row=2,column=0,columnspan=4,rowspan=4,padx=10,pady=10)


# Labels in frame
frame_label = Label(theframe,text="File Menu", font=("TimeRoman",30))

frame_label.pack()


frame_label2 = Label(theframe2,text="Edit Menu", font=("Ariel",30))

frame_label2.pack()

root.mainloop()

