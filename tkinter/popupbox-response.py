from tkinter import * 
from tkinter import messagebox
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



#adding text to the screen
mylabel = Label(root,text="type you name", font=("TimeRoman", 32))
mylabel.pack()




# button function what happens when you click
def popup():
    response = messagebox.askokcancel("Popup Title", "Looking good")
    mylabel= Label(root,text=response).pack()

    if response == 1:
        mylabel= Label(root,text="performing action1").pack()
    else:
        mylabel= Label(root,text="performing action2").pack()
#showinfo showwarning showerror askquestion askokcancel askyesno
mybutton = Button(root,text="clickme", command=popup)
mybutton.pack()


root.mainloop()