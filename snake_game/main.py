from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

TIMER = 0.1
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)
segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
is_on = True

while is_on:
    screen.update()
    time.sleep(TIMER)
    snake.move()

    #Detect collision with a food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    #Detect collision with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() <-290:
        is_on = False
        scoreboard.game_finish()

    #Detect collision with a tail
       #trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_finish()

screen.exitonclick()
