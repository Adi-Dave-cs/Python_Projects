from ctypes import alignment
import time
from turtle import Screen, Turtle, heading

sc = Screen()
sc.bgcolor('black')
sc.setup(width = 800 , height= 600)
sc.tracer(0)
sc.title("Pong_Game")

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1 , stretch_wid=5)
        self.penup()
        self.goto(pos)
    def go_up(self):
        ncor = self.ycor() + 20
        self.goto(self.xcor(),ncor)

    def go_down(self):
        ncor = self.ycor() - 20
        self.goto(self.xcor(),ncor)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align = 'center' , font=("Courier" , 80 , "normal"))
        self.goto(100,200)
        self.write(self.r_score,align = 'center' , font=("Courier" , 80 , "normal"))
    
    def l_point(self):
        self.l_score += 1
        self.score_update()
    
    def r_point(self):
        self.r_score += 1
        self.score_update()


class Ball(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(pos)
        self.move_speed = 0.1
        self.x = 10
        self.y = 10
    def move(self):
        ncor = self.ycor() + self.y
        mcor = self.xcor() + self.x
        self.goto(mcor,ncor)
    
    def bounce_y(self):
        self.y *= -1
    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
        

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
c_ball = Ball((0,0))


sc.listen()
sc.onkey(r_paddle.go_up,"Up")
sc.onkey(r_paddle.go_down,"Down")
sc.onkey(l_paddle.go_up,"w")
sc.onkey(l_paddle.go_down,"s")

game_on = True
scb = Scoreboard()
while(game_on):
    time.sleep(c_ball.move_speed)
    sc.update()
    c_ball.move()
    if(c_ball.ycor() > 280 or c_ball.ycor() < -280):
        c_ball.bounce_y()
    
    if((c_ball.distance(r_paddle) < 50 and c_ball.xcor() > 320) or (c_ball.distance(l_paddle) < 50 and c_ball.xcor() < -320)):
        c_ball.bounce_x()
    
    if(c_ball.xcor() > 380 ):
        scb.l_point()
        c_ball.reset_position()
    if(c_ball.xcor() < -380):
        scb.r_point()
        c_ball.reset_position()

sc.exitonclick()