import requests
from tkinter import *
from generate import *
import time


bg = '#627AF6'
RED = "#C05039"
GREEN = '#33DA3D'
score = 0
cnt = 0
def start_game(root,n , color):
    p = n
    def right_click():
        global score , cnt
        if(cnt > p):
            root1.destroy()
        if(questions[cnt][1]=='True'):
            score = score + 1
            cv.configure(background=GREEN)
            s = "Score : " + str(score)
            a.configure(text=s)
        else:
            cv.configure(background=RED)

        cnt = cnt + 1
        if(cnt == p):
            s = ""
            a.configure(text=s)
            cv.configure(background='white')
            s = "Your Score : " + str(score)
            cv.itemconfig(textf,text=s)
            cnt = cnt + 1
            return
        if(cnt > p):
            root1.destroy()
        time.sleep(2)
        # cv.configure(background='white')
        cv.itemconfig(textf,text=questions[cnt][0])

    def wrong_click():
        global cnt,score
        if(cnt > p):
            root1.destroy()
        if(questions[cnt][1]=='True'):
            score = score + 1
            cv.configure(background=GREEN)
            s = "Score : " + str(score)
            a.configure(text=s)
        else:
            cv.configure(background=RED)
            
        cnt = cnt + 1
        if(cnt == p):
            s = ""
            a.configure(text=s)
            cv.configure(background='white')
            s = "Your Score : " + str(score)
            cv.itemconfig(textf,text=s)
            cnt = cnt + 1
            return
        if(cnt > p):
            root1.destroy()
        time.sleep(2)
        # cv.configure(background='white')
        cv.itemconfig(textf,text=questions[cnt][0])
        
    root1 = Toplevel(root)
    root1.title("Quizzy")
    root1.config(padx=50,pady=50,background="#627AF6")
    questions = generateQ(p)
    a = Label(root1,text="Score : 0" , font=('ariel 15 bold'),bg='#627AF6',fg='white')
    a.grid(row = 0 , column=1)
    cv = Canvas(root1,width = 1000,height=200,background="white",highlightbackground='#030E47',highlightthickness=5)
    textf = cv.create_text(500,100,width=500,text=questions[cnt][0],font=('Arial' , 15 , 'bold'),justify=CENTER)
    cv.grid(row = 1,column=0,columnspan=2,pady = 10 )


    wrong = PhotoImage(file="D:\\ADITYA IMPORTANT PDF\\Codes\\python\\Tkinter_python\\Flash_card_game\\images\\wrong.png")
    cross_btn = Button(root1,image=wrong, command=wrong_click ,highlightthickness=0)
    cross_btn.grid(row=2,column=0,pady=10)
    right = PhotoImage(file="D:\\ADITYA IMPORTANT PDF\\Codes\\python\\Tkinter_python\\Flash_card_game\\images\\right.png")
    tick_btn = Button(root1,image=right , command=right_click ,highlightthickness=0)
    tick_btn.grid(row=2,column=1,pady = 10)

    root1.mainloop()

# start_game(5,"blue")