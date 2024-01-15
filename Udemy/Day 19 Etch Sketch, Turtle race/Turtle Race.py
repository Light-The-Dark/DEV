# TODO make each turtle moves a random amount
import random
from turtle import *

colors = ["red", "blue","green","purple","yellow","orange"]
turtles = []
screen = Screen()
screen.setup(width=500,height=500)
race_is_on = True

def initalize():
    
    i = 0
    x = -200
    y = -125

    for _ in range(6):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].setposition(x, y)
        
        y += 50
        i += 1


def race():
    global race_is_on
    i = 0
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        x, y = turtle.position()
        if x >= 220:
            race_is_on = False
            return i
        i += 1
    return True

initalize()
bet = textinput("TURTLE RACE!!!", "Which turtle would you like to bet on?")

while race_is_on == True:
    i = race()

color = turtles[i].pencolor()
if bet == color:
    print("you won")
else:
    print("you lost")
print(f"{color} turtle wins!")









screen.exitonclick()

