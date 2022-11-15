from tkinter import *
import pandas as pd
import random 

r = ''

def wrong_click():
    img1 = PhotoImage(file='images/card_back.png')
    cv.itemconfig(card,image=img1)
    cv.itemconfig(title,text="English")
    cv.itemconfig(word,text = r["English"])
    
    return

def right_click():
    global r
    r = random.choice(to_learn)
    cv.itemconfig(card,image=img)
    cv.itemconfig(title,text="French")
    cv.itemconfig(word,text=r["French"])
    return
BACKGROUND_COLOR = "#B1DDC6"
root = Tk()
root.title("Flash Card game")
root.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)

try : 
    data = pd.read_csv("data/french_words.csv")
    to_learn =data.to_dict(orient='records')
except:
    print("The file does not exist")


cv = Canvas(width=800 , height=526 , highlightthickness=0,background=BACKGROUND_COLOR)
img = PhotoImage(file='images/card_front.png')
card = cv.create_image(400,263,image=img)
title = cv.create_text(400,150,text="French <=> English",font=("Ariel",35,"italic"))
word = cv.create_text(400,263,text="word",font=("Ariel",30,"bold"))
cv.grid(row=0,column=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=wrong, command=wrong_click ,highlightthickness=0)
cross_btn.grid(row=1,column=0)
right = PhotoImage(file="images/right.png")
tick_btn = Button(image=right , command=right_click ,highlightthickness=0)
tick_btn.grid(row=1,column=1)

root.mainloop()