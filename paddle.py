from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, min_x, max_x, position=(0, 0)):
        super().__init__()
        self.shape("square")
        self.color("#A7ADBA")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.start_position = position
        self.goto(self.start_position)
        self.min_x = min_x
        self.max_x = max_x

    def move_left(self):
        if self.xcor() > self.min_x:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < self.max_x:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(self.start_position)