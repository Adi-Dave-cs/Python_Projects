# tutorial for the same can be found at : https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

cur = Turtle()
screen = Screen()

def move_forward():
    cur.forward(10)

def move_left():
    cur.left(10)

def move_right():
    cur.right(10)

def move_backward():
    cur.backward(10)

def clear():
    cur.clear()
    cur.penup()
    cur.home()
    cur.pendown()

screen.listen()
screen.onkey(move_forward,'w')
screen.onkey(move_left,'a')
screen.onkey(move_backward,'s')
screen.onkey(move_right,'d')
screen.onkey(clear,'c')
screen.exitonclick()
