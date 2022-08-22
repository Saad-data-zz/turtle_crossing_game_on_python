from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
      self.all_cars = []
      self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            #setting the shape of car
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            #assigning color to cars
            new_car.color(random.choice(COLORS))
            #location for the car where the cars coming
            random_y = random.randint(-260,260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    #everytime when the turtle appear's the speed incremenrt about 10
    def level_up(self):
        self.car_speed +=MOVE_INCREMENT