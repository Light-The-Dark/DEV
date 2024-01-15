from turtle import *
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        
    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
        