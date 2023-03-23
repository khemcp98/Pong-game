from turtle import Turtle

FONT = ('Arial', 15, 'normal')
ALIGN = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

    def display_score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.write(f"Score: {self.l_score} | {self.r_score}", align=ALIGN, font=FONT)

    def l_refresh_score(self):
        self.display_score()
        self.clear()
        self.l_score += 1

    def r_refresh_score(self):
        self.display_score()
        self.clear()
        self.r_score += 1
