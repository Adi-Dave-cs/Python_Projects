import random
import time
from turtle import Screen,Turtle


colors = ["red","orange" ,"blue" ,"yellow" ,"green" ,"purple"]

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        r = random.randint(1,6)
        if(r == 1):
            new_Car = Turtle()
            new_Car.shape("square")
            new_Car.shapesize(stretch_len=2,stretch_wid=1)
            new_Car.penup()
            new_Car.color(random.choice(colors))
            ny = random.randint(-250,250)
            new_Car.goto(300,ny)
            self.all_cars.append(new_Car)
    
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


sc = Screen()
scb = Scoreboard()
sc.bgcolor('white')
sc.setup(width=600 , height= 600)
sc.tracer(0)
pl = Player()
car_manager = CarManager()
sc.listen()
sc.onkey(pl.go_up,"Up")


game_on = True
while(game_on):
    time.sleep(0.1)
    sc.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if(car.distance(pl) < 20):
            game_on = False
            scb.game_over()
    if(pl.is_at_finish_line()):
        pl.go_to_start()
        car_manager.level_up()
        scb.increase_level()
sc.exitonclick()