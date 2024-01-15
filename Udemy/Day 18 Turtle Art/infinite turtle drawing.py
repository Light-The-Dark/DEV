from turtle import *
import random

joe = Turtle()
i = 3
colormode(255)
joe.speed("fastest")

while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    joe.pencolor((r, g, b))
    for _ in range(i):
        joe.right(360 / i)
        joe.forward(50)
    i += 1




screen = Screen()
screen.exitonclick()