from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-280, 260)
        self.next_level()

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align = 'left', font = FONT)

    def game_over(self):
        self.goto(0, -15)
        self.write(f"Game over.", align = 'center', font = FONT)