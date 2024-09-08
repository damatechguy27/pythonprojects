from tkinter import * 
from tkinter import ttk
from os.path import join
from PIL import Image, ImageTk
icon = join('resources','currency_dollar_icon.ico')
img = join('resources','moon.jpg')


#tkinter instance
root = Tk()

# add in icons 
root.iconbitmap(icon)

#add title to caption
root.title("Day of the week")

#adding window size 
root.geometry("1280x720")


#adding text to the screen
mylabel = Label(root,text="Favorite day of the week", font=("TimeRoman", 32))
mylabel.pack()


# options for your combobox
options = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"
]

mycombo = ttk.Combobox(root,values=options)
mycombo.current(0)
mycombo.pack()

# button function what happens when you click
def selectday():
    if mycombo.get() == "sunday":
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "monday":
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "tuesday":        
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "wednesday":        
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "thrusday":        
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "friday":        
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()
    elif mycombo.get() == "saturday":        
        mylabel2 = Label(root, text=f"Your favorite day is {mycombo.get()}")
        mylabel2.pack()


#showinfo showwarning showerror askquestion askokcancel askyesno
mybutton = Button(root,text="clickme", command=selectday)
mybutton.pack()

root.mainloop()