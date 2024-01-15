UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


from turtle import *

class Snake(Turtle):

    def __init__(self) -> None:
        self.snakes = []
        self.x = 0
        self.y = 0
        for _ in range(3):
            self.add_piece()  
            self.x -= 20  
        self.head = self.snakes[0]

    def add_piece(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.setposition(self.x, self.y)
        self.snakes.append(snake)
        

    def extend(self):
        self.x, self.y = self.snakes[-1].position()
        self.add_piece()

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
