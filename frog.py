from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 25
FINISH_LINE_Y = 260


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.go_to_start()
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
 
    def move_up(self):
        if self.heading() != 90:
            self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.heading() != 270:
            self.setheading(270)
        if self.ycor() > -260:
            self.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.heading() != 0:
            self.setheading(0)
        if self.xcor() < 280:
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.heading() != 180:
            self.setheading(180)
        if self.xcor() > -280:
            self.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    

    