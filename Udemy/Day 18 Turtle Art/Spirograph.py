from turtle import *
import random

nan = Turtle()
heading = 0
colormode(255)
nan.speed("fastest")

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    nan.pencolor((r, g, b))

while heading < 360:
    change_color()
    nan.setheading(round(heading, 2))
    nan.circle(100)
    heading += 3.6
    
    # Prints differences in numbers that you could play with by changing code above
    print(round(heading, 2))
    print(round(heading))
    print(heading)




screen = Screen()
screen.exitonclick()