from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

player2 = Paddle(-350, 20)
player1 = Paddle(350, 20)
ball = Ball()
score = Score()


screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.display_score()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if left paddle miss ball
    if ball.xcor() > 390:
        ball.reset_ball()
        score.l_refresh_score()

    # Detect if right paddle miss ball
    if ball.xcor() < -390:
        ball.reset_ball()
        score.r_refresh_score()


screen.exitonclick()
