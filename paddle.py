from turtle import Turtle

MOVE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=3.5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), y=new_y)
