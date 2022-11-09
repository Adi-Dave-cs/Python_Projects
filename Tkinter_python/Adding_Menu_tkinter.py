from tkinter import *

#root for initializing the tkinter object

root = Tk()

# root window title and dimension

root.title("Third Program")

# Set geometry (widthxheight)

root.geometry('400x400')

# we create a Label widget as a child to the root window

a = Label(root, text='Hey ssup?')
a.grid()

# adding menu bar in root window new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)
 

# function to display text when button is clicked
def clicked():
    res = "Hello "
    c = Label(root,text = res)
    c.grid(row=0,column=2)

# button widget with red color text inside
btn = Button(root , text = 'Click Here !!' ,fg = 'red', command=clicked)
btn.grid(column=1,row=0)

root.mainloop()