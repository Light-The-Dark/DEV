from turtle import *

bob = Turtle()

bob.shape("turtle")
bob.color("skyblue")

for _ in range(10):
    bob.pendown()
    bob.forward(10)
    bob.penup()
    bob.forward(10)








screen = Screen()
screen.exitonclick()