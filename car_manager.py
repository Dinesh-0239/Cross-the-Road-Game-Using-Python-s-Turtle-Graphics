from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
INCREMENT_SPEED = 10
MOVE_INCREMENT = 10
START_XPOS = 300
START_RANGE_POS = -250
END_RANGE_POS = 250
CAR_SHAPE = "square"
CAR_WIDTH = 1
CAR_LEN = 2
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = MOVE_INCREMENT
    def create_cars(self):
        random_chance = randint(1,4)
        if random_chance == 1:
            new_car = Turtle(CAR_SHAPE)
            new_car.shapesize(stretch_len=CAR_LEN,stretch_wid=CAR_WIDTH)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(START_RANGE_POS,END_RANGE_POS)
            new_car.goto(START_XPOS,random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
    def get_cars(self):
        return self.all_cars

    def level_up(self):
        self.car_speed += INCREMENT_SPEED