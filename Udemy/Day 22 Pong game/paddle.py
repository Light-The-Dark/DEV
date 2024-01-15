from turtle import *

X = 350
Y = 0

class player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pu()
        self.setposition(position)

    def go_up(self):
        x, y = self.position()
        self.setposition(x, y + 20)

    def go_down(self):
        x, y = self.position()
        self.setposition(x, y - 20)


  



