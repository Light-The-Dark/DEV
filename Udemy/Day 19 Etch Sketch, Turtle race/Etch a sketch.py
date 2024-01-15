# TODO wasd movement, c = clear screen


from turtle import *

bob = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    bob.forward(10)


def move_backwards():
    bob.backward(10)


def turn_left():
    bob.left(10)


def turn_right():
    bob.right(10)


def clear():
    bob.clear()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)




screen.exitonclick()