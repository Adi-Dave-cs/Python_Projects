from tkinter import *

#root for initializing the tkinter object

root = Tk()

# root window title and dimension

root.title("Second Program")

# Set geometry (widthxheight)

root.geometry('400x400')

# we create a Label widget as a child to the root window

a = Label(root, text='What is yout name?')
a.grid()

txt = Entry(root,width=20)
txt.grid(row=0,column=1)

# function to display text when button is clicked
def clicked():
    res = "Hello " + txt.get()
    c = Label(root,text = res)
    c.grid(row=0,column=3)

# button widget with red color text inside
btn = Button(root , text = 'Click Here !!' ,fg = 'red', command=clicked)
btn.grid(column=2,row=0)

root.mainloop()