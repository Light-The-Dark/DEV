from turtle import *

FONT = ("Arial", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("C:/Users/alazarix/files/snake_high_score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center" , font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            new_high_score = str(self.highscore)
            with open("C:/Users/alazarix/files/snake_high_score.txt", mode="w") as high_score_txt:
                high_score_txt = high_score_txt.write(new_high_score)
            
        self.score = 0
        self.update_scoreboard()


