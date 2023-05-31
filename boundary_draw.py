from turtle import Turtle

BOUNDARY_Y_COORDINATES = [-265, -15, 10, 260]
ROAD_LINE_Y_COORDINATES = range(-240, 240, 25)

class Boundary_Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')

        for y in BOUNDARY_Y_COORDINATES:
            self.penup()
            self.goto(-300, y)
            self.pendown()
            self.goto(300, y)

        self.penup()
        self.color('yellow')

        for y in ROAD_LINE_Y_COORDINATES:
            if y <= 10 and y >= -15:
                continue
            self.goto(-300, y)
            if y % 2 == 0:
                self.pendown()
            else:
                self.penup()
            for _ in range(-300, 300, 40):
                self.forward(20)
                if self.isdown():
                    self.penup()
                else:
                    self.pendown()
                self.forward(20)
                if self.isdown():
                    self.penup()
                else:
                    self.pendown()
            self.penup()


        