from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
import scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

ball = Ball()
scoreboard = scoreboard.Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.y_bounce()

    #Detect with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.x_bounce()

    #Misses tge paddles
    if ball.xcor() > 395:
        ball.paddle_miss()
        scoreboard.l_point()
    elif ball.xcor() <-395:
        ball.paddle_miss()
        scoreboard.r_point()

screen.exitonclick()