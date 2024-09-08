from tkinter import * 
from os.path import join
from tkinter import filedialog
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
mylabel = Label(root,text="click button to open file", font=("TimeRoman", 32))
mylabel.pack()

# button function what happens when you click
def selectfile():
    root.filename = filedialog.askopenfilename(initialdir='./', title="open image file",filetypes=(("PNG Files", "*.png"), ("All Files", ".*")))
    #add images
    global images
    images= ImageTk.PhotoImage(Image.open(root.filename))

    imagelabel = Label(root,image=images)

    imagelabel.pack()


#showinfo showwarning showerror askquestion askokcancel askyesno
mybutton = Button(root,text="clickme", command=selectfile)
mybutton.pack()




root.mainloop()


#working with grids 
#mylabel2 = Label(root,text="examing grid")
#mylabel2.grid(row=0,column=20)

