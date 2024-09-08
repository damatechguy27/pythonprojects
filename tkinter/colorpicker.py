from tkinter import * 
from tkinter import colorchooser
from os.path import join
icon = join('resources','currency_dollar_icon.ico')

#tkinter instance
root = Tk()

# add in icons 
root.iconbitmap(icon)

#add title to caption
root.title("Hello World")

#adding window size 
root.geometry("1280x720")

mylabel = Label(root,text="Choose Color", font=("TimeRoman", 32))
mylabel.pack()


def selectcolor():
    # returns colors in a list
    mycolor = colorchooser.askcolor()[1]

    mylabel2 = Label(root,text=mycolor).pack()

    # test makes the label the color selected
    mylabel2 = Label(root,text="your color", bg=mycolor).pack()



mybutton = Button(root,text="clickme", command=selectcolor)
mybutton.pack()



root.mainloop()