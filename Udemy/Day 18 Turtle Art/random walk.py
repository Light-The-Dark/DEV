from turtle import *
import random

directions = [0, 90, 180, 270]
joe = Turtle()
colormode(255)
joe.speed("fastest")
joe.pensize(5)


def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    joe.pencolor((r, g, b))


while True:
    change_color()
    joe.setheading(random.choice(directions))
    joe.forward(10)





screen = Screen()
screen.exitonclick()