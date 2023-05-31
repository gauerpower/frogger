from turtle import Turtle, register_shape
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

for color in COLORS:
    register_shape(f'./images/car_icon_{color}.gif')

class Road:

    def __init__(self):
        self.car_collection = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 5) == 1:
            y_coord = random.randint(-10, 10) * 25
            while y_coord <= 10 and y_coord >= -10:
                y_coord = random.randint(-10, 10) * 25
            for car in self.car_collection:
                if y_coord == car.ycor() and abs(car.xcor() in range(220, 300)):
                    return
            next_car = Turtle(f'./images/car_icon_{random.choice(COLORS)}.gif')
            next_car.penup()
            next_car.color(random.choice(COLORS))
            if y_coord >= 0:
                next_car.goto(-300, y_coord)
            else:
                next_car.setheading(180)
                next_car.goto(300, y_coord)
            self.car_collection.append(next_car)

    def move_cars(self):
        for car in self.car_collection:
            car.forward(STARTING_MOVE_DISTANCE)

    def delete_offscreen_cars(self):
        for i in range(len(self.car_collection) - 1, -1, -1):
            if abs(self.car_collection[i].xcor()) > 320:
                self.car_collection[i].hideturtle()
                self.car_collection.remove(self.car_collection[i])