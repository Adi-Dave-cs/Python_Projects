from tkinter import *
import calendar
root = Tk()

root.geometry("300x300")

a = Label(root,text="Enter the year")
a.grid()

b = Entry(root,width = 10)
b.grid(row=0,column=2)


def fetch():
    gui1 = Tk()
    gui1.title("CALENDAR")
    gui1.geometry("400x400")
    yr = int(b.get())
    f = calendar.calendar(yr)
    cal_year = Label(gui1, text = f, font = "Consolas 10 bold")
    cal_year.pack()
    gui1.mainloop()

c = Button(root,text="Fetch the calendar",fg = "Red" ,command=fetch)
c.grid(row=1,column=1)

d = Button(root,text="Exit",fg = "Red" ,command=exit)
d.grid(row=2,column=1)

root.mainloop()

