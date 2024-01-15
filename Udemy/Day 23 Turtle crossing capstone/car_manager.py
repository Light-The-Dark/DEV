import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        if random.randint(1,6) == 1:
            car = turtle.Turtle("square")
            car.pu()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setposition(280, random.randint(-250, 250))
            car.setheading(180)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.fd(self.move_distance)

    def level_up(self):
        self.cars = []
        self.move_distance += MOVE_INCREMENT



