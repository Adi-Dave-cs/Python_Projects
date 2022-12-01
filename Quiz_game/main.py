import requests
from tkinter import *
from start_game import *
def blue():
    start_game(root,5, "blue")
def green():
    start_game(root,10 ,"green")
def red():
    start_game(root,15 , "red")
def pink():
    start_game(root,20 , "pink")

root = Tk()
root.title("Quizzy")
root.config(padx=50 , pady=50 ,background="yellow")

d = Label(root, text="Press the buttons to select number of questions" , font=('arial 12 bold italic'))
d.grid(row = 0,column=0)
a = Button(root,text="5 Questions" , fg= "white",justify= CENTER,font=('Courier 10 bold'), background='blue' , command=blue)
a.grid(row=1,column=0,pady=5)
b = Button(root,text="10 Questions" , fg= "white", justify= CENTER,font=('Courier 10 bold'), background='green' , command=green)
b.grid(row=2,column=0,pady=5)
c = Button(root,text="15 Questions" , fg= "white", justify= CENTER,font=('Courier 10 bold'), background='red' , command=red)
c.grid(row=3,column=0,pady=5)
d = Button(root,text="20 Questions" , fg= "white", justify= CENTER,font=('Courier 10 bold'), background='black' , command=pink)
d.grid(row=4,column=0,pady=5)
d = Button(root,text="EXIT" , fg= "white", justify= CENTER,font=('Courier 10 bold'), background='RED' , command=exit)
d.grid(row=5,column=0,pady=5)

root.mainloop()