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
root.title("Creating new windows")

#adding window size 
root.geometry("1280x720")

# create new window
#new = Toplevel()


#function to open new window
def openwindow():
    # create new window
    new = Toplevel()
    #tkinter instance

    # add in icons 
    new.iconbitmap(icon)

    #add title to caption
    new.title("The new windows")

    #adding window size 
    new.geometry("400x400")

    #add images
    image= ImageTk.PhotoImage(Image.open(img))

    imagelabel = Label(new,image=image)

    imagelabel.pack()


    #adding text to the screen
    mylabel = Label(new,text="you like the second window", font=("TimeRoman", 32))
    mylabel.pack()

    #minimize window into a icon on screen
    hide_button = Button(new,text="hide", command=root.iconify)
    
    #display window
    show_button = Button(new,text="show", command=root.deiconify)

    # withdraw window removes window without minimizing it 
    withdraw_button = Button(new,text="withdraw", command=root.withdraw)

    # destroy window kills entire program
    destroy_button = Button(new,text="destroy", command=root.destroy) 
    
    hide_button.pack()
    show_button.pack()
    withdraw_button.pack()
    destroy_button.pack()

    new.mainloop()


#using button to get a second window to pop up
mybutton = Button(root,text="clickme", command=openwindow)
mybutton.pack()




root.mainloop()

