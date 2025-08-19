from turtle import Turtle
POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(POSITION)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(POSITION)

