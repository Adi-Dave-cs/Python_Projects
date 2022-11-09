from tkinter import *

#root for initializing the tkinter object

root = Tk()

# root window title and dimension

root.title("Fourth Program")

# Set geometry (widthxheight)

root.geometry('400x400')


def clicked():
    # Adding the elements in the listbox
    top = Tk()
    top.title('New Window')
    Lb = Listbox(top)
    Lb.insert(1, 'Python')
    Lb.insert(2, 'Java')
    Lb.insert(3, 'C++')
    Lb.insert(4, 'Any other')
    Lb.pack()
    top.mainloop()

# adding checkbox
var1 = IntVar()
Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W)
btn = Button(root,text='Click me!!' , command=clicked,fg='red')
btn.grid()

# Adding menu to the tkinter
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


root.mainloop()