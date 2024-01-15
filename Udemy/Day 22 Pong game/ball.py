from turtle import *

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("blue")
        self.x = 5
        self.y = 5
        self.move_speed = .05

    def move(self, x, y):
        self.setposition(x + self.x, y + self.y)
    
    def bounce_y(self):
         self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= .9

    def restart(self):
        self.setposition(0, 0)
        self.bounce_x()
        self.move_speed = .05