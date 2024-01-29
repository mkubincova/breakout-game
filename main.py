from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

BRICK_POSITIONS_X = [-330, -265, -200, -135, -70, -5, 60, 125, 190, 255, 320]
BRICK_POSITIONS_Y = [240, 215, 190, 165, 140]
BRICK_COLORS = ["#F87171", "#5FA6FA", "#FB923C", "#FACC14", "#4CDE81", "#5FA6FA"]

screen = Screen()
screen.bgcolor("#1D232A")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(position=(0, -270), min_x=-350, max_x=350)
ball = Ball(position=(0, -240))
bricks = []

for x in BRICK_POSITIONS_X:
    for y in BRICK_POSITIONS_Y:
        color = BRICK_COLORS[BRICK_POSITIONS_Y.index(y)]
        new_brick = Brick(color)
        new_brick.goto(x, y)
        bricks.append(new_brick)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(ball.start_moving, "space")

is_playing = True

while is_playing:
    time.sleep(ball.move_speed)
    screen.update()

    if not ball.is_moving:
        ball.move_horizontally(paddle.xcor())
    else:
        ball.move()

        # Detect collision with wall
        if ball.xcor() > 370 or ball.xcor() < -380:
            ball.bounce_x()

        if ball.ycor() > 280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.ycor() == -250 and ball.distance(paddle) <= 63:
            ball.bounce_y()
            ball.move_speed *= 0.9

        # Detect collision with brick
        for brick in bricks:
            if ball.distance(brick) <= 43:
                if abs(brick.xcor() - ball.xcor()) <= 40:
                    ball.bounce_x()
                    brick.hideturtle()
                    bricks.remove(brick)
                elif abs(brick.ycor() - ball.ycor()) <= 20:
                    ball.bounce_y()
                    brick.hideturtle()
                    bricks.remove(brick)

        # Detect paddle miss
        if ball.ycor() < -280:
            paddle.reset_position()
            ball.reset_position()

screen.exitonclick()
