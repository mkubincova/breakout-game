from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_y = 10
        self.move_x = 10
        self.move_speed = 0.08
        self.starting_position = position
        self.goto(self.starting_position)
        self.is_moving = False

    def start_moving(self):
        self.is_moving = True

    def move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(new_x, new_y)

    def move_horizontally(self, new_x):
        self.goto(new_x, self.ycor())

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(self.starting_position)
        self.is_moving = False
        self.bounce_y()

