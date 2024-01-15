import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def initialize():
    global screen, turtle
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    turtle = Player()
    screen.onkey(turtle.move, "w")

initialize()


sboard = Scoreboard()
cars = CarManager()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.add_car()

    if turtle.ycor() == 280:
        screen.clear()
        initialize()
        turtle.reset()
        sboard.update_level()
        cars.level_up()
        

    for car in cars.cars:
        if car.distance(turtle) < 25:
            game_is_on = False


sboard.game_over()
screen.update()
screen.exitonclick()