from tkinter import *
main = Tk()
main.geometry('400x400')
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop( )
