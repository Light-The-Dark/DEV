from turtle import *


FONT = ("Arial", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.setposition(-250, 250)
        self.write(f"Score: {self.l_score}", align="center" , font=FONT)
        self.setposition(250, 250)
        self.write(f"Score: {self.r_score}", align="center" , font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
