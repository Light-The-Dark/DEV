import scoreboard
import paddle
from turtle import *
import ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

bal = ball.Ball()
score = scoreboard.ScoreBoard()

player1 = paddle.player((350, 0))
player2 = paddle.player((-350, 0))

screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_on = True
sleep = .05

while game_on:

    time.sleep(bal.move_speed)
    screen.update()

    # Detects if ball hits the paddle, bounces back, and speeds up ball if hit
    if bal.distance(player1) < 60 and bal.xcor() == 330 or bal.distance(player2) < 60 and bal.xcor() == -330:
        bal.bounce_x()
        sleep *= .9
    # Detects if ball hits top of the screen
    elif bal.ycor() >= 260 or bal.ycor() <= - 260:
        bal.bounce_y()
    # Detects if paddle missed ball, adds score, and restarts speed and ball position
    elif bal.xcor() > 380:
        score.l_score += 1
        bal.restart()
    elif bal.xcor() < -380:
        score.r_score += 1
        bal.restart()


    bal.move(bal.xcor(), bal.ycor())
    score.update_score()


    #Stops game if score hits 10
    if score.l_score == 10 or score.r_score == 10:
        game_on = False
        score.game_over()

screen.exitonclick()

