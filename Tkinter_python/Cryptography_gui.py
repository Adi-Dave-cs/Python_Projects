from tkinter import *
import hashlib
from tkinter import ttk 
import onetimepad as otp

root = Tk()

root.title("Cryptography Using Tkinter")

root.geometry("600x300")

a = Label(root , text="Enter the text to encode", fg='red')
a.grid()

b = Entry(root , width=20)
b.grid(row=0, column=1)

ttk.Separator(root, orient=VERTICAL).grid(column=2, row=0)

c = Label(root,text="Enter the hashcode to decipher", fg = 'blue')
c.grid(row=0,column=3)

d = Entry(root , width=20)
d.grid(row=0, column=4)

def decipher():
    ans = d.get()
    ans = otp.decrypt(ans,'random')
    d.delete(0,END)
    d.insert(0,ans)

def cipher():
    ans = b.get()
    ans = otp.encrypt(ans,'random')

    b.delete(0,END)
    b.insert(0,ans)

e = Button(root, text = "Encrypt", fg='white' , command=cipher,background='green')
e.grid(row=1,column=0)

f = Button(root, text = "Decrypt", fg='red' , command=decipher ,background='yellow')
f.grid(row=1,column=3)


root.mainloop()