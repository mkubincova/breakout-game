from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color="red"):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color(color)
