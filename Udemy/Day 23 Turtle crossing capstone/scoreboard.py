import turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 0
        self.setposition(0, 250)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
        

