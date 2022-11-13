from tkinter import *

PINK="#e2979c"
RED="#e7305b"
GREEN="#9deacf"
YELLOW="#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
def start_button():
    global reps
    reps += 1
    if(reps%2 == 0 and reps%2==8):
        count_down(LONG_BREAK_MIN*60)
        title_label.config(text="BREAK" , fg=RED)
    elif(reps%2==0):
        count_down(SHORT_BREAK_MIN*60)
        title_label.config(text="BREAK" , fg=PINK)
    else:
        count_down(WORK_MIN*60)
        title_label.config(text="WORK" , fg=GREEN)

def count_down(n):
    count_min = int(n/60)
    count_sec = int(n%60)
    if(count_sec < 10):
        count_sec = "0"+str(count_sec)
    if(count_min < 10):
        count_min = "0"+str(count_min)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if(n>0):
        global timer
        timer = root.after(1000,count_down,n-1)

def reset_button():
    global reps
    reps = 0
    root.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    return
root = Tk()
root.title("Pomodoro")
root.config(padx=50 , pady=50 , background=YELLOW )

title_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME,25,"bold"))
title_label.grid(row=0,column=1)

canvas = Canvas(width=200 , height=224 ,background=YELLOW,border=0)
image_ep = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=image_ep)
timer_text = canvas.create_text(103,112,text="00:00" , fill="white",font = (FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

start = Button(text="start" , highlightthickness=0,font=(FONT_NAME,15,"bold"),command=start_button)
start.grid(row=3,column=0)
end = Button(text="exit" , highlightthickness=0 ,font=(FONT_NAME,15,"bold"),command=exit)
end.grid(row=3,column=1)
reset = Button(text="reset" , highlightthickness=0,font=(FONT_NAME,15,"bold"),command=reset_button)
reset.grid(row=3,column=2)
root.mainloop()