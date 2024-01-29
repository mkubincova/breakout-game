from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from score import ScoreBoard
import time


def create_bricks():
    for x in BRICK_POSITIONS_X:
        for y in BRICK_POSITIONS_Y:
            color = BRICK_COLORS[BRICK_POSITIONS_Y.index(y)]
            new_brick = Brick(color)
            new_brick.goto(x, y)
            bricks.append(new_brick)


BRICK_POSITIONS_X = [-330, -265, -200, -135, -70, -5, 60, 125, 190, 255, 320]
BRICK_POSITIONS_Y = [240, 215, 190, 165, 140]
BRICK_COLORS = ["#F87171", "#5FA6FA", "#FB923C", "#FACC14", "#4CDE81", "#5FA6FA"]

screen = Screen()
screen.bgcolor("#1D232A")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

scoreboard = ScoreBoard(screen_w=800, screen_h=600, lives=3)
paddle = Paddle(position=(0, -265), min_x=-350, max_x=350)
ball = Ball(position=(0, -240))
bricks = []
create_bricks()

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
        if ball.ycor() == -250 and ball.distance(paddle) <= 67:
            ball.bounce_y()
            ball.move_speed *= 0.9

        # Detect collision with brick
        for brick in bricks:
            if ball.distance(brick) <= 43:
                if abs(brick.xcor() - ball.xcor()) <= 40 or abs(brick.ycor() - ball.ycor()) <= 20:
                    brick.hideturtle()
                    bricks.remove(brick)
                    if len(bricks) == 0:
                        create_bricks()
                    scoreboard.increase_score()
                if abs(brick.xcor() - ball.xcor()) <= 40:
                    ball.bounce_x()
                elif abs(brick.ycor() - ball.ycor()) <= 20:
                    ball.bounce_y()

        # Detect paddle miss
        if ball.ycor() < -280:
            paddle.reset_position()
            ball.reset_position()
            scoreboard.decrease_lives()
            if scoreboard.lives == 0:
                is_playing = False
                scoreboard.game_over()


screen.exitonclick()
