# https://www.geeksforgeeks.org/python-tkinter-tutorial/

from tkinter import *

#root for initializing the tkinter object

root = Tk()

# root window title and dimension

root.title("First Program")

# Set geometry (widthxheight)

root.geometry('400x400')

# we create a Label widget as a child to the root window

a = Label(root, text='Hello , world!')

# function to display text when button is clicked
def clicked():
    a.configure(text = "I just got clicked")
    a.grid(column=2,row=0)

# we call the pack() method on this widget. This tells it to size itself to fit the given text, and make itself visible

a.grid()

# button widget with red color text inside
btn = Button(root , text = 'Do Not Click here !!' ,fg = 'red', command=clicked)
btn.grid(column=1,row=0)

root.mainloop()