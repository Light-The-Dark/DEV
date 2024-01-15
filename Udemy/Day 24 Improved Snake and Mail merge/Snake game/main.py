SLEEP = .1

import food
from turtle import *
import time
import snake
import scoreboard

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.ScoreBoard()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)

game_over = False

while game_over == False:

    screen.update()
    time.sleep(SLEEP)   
    snake.move()

    # Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.restart()

    # Detects collision with self
    for piece in snake.snakes[1:]:
        if snake.head.distance(piece) < 10:
            scoreboard.reset_score()
            snake.restart()

        
screen.exitonclick()
