from turtle import Turtle
FONT = ("Arial", 20, "normal")
FONT_SM = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self, screen_w=500, screen_h=500, lives=5):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.start_lives = lives
        self.lives = self.start_lives
        self.width = screen_w
        self.height = screen_h
        self.print_scoreboard()

    def increase_score(self):
        self.score += 1
        self.print_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.setx(self.width / 2 * -1 + 15)
        self.sety(self.height / 2 - 35)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.setx(self.width / 2 - 20)
        self.write(f"{' ❤' * self.lives}", align="right", font=FONT)
        self.setx(self.width / 2 * -1 + 15)
        self.sety(self.height / 2 * -1 + 20)
        self.write("Press 'space' to start the game.", align="left", font=FONT_SM)

    def game_over(self):
        self.setx(0)
        self.sety(0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        self.score = 0
        self.lives = self.start_lives
        self.print_scoreboard()
