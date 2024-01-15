from turtle import *
import random

hirst = Turtle()
y = -250
hirst.hideturtle()
hirst.penup()
hirst.pensize(5)
hirst.speed("fastest")
colormode(255)


def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    hirst.pencolor((r, g, b))


for _ in range(11):
    x = -250
    hirst.setposition(x, y)
    for _ in range(11):
        change_color()
        hirst.dot(20)
        hirst.forward(50)
    y += 50




screen = Screen()
screen.exitonclick()

