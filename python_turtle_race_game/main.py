from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a colour")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]
turtles = []

y = -100

for turtle_index in range(0,8):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colours[turtle_index])
    my_turtle.penup()
    my_turtle.goto(x=-230, y=y)
    y +=30
    turtles.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle is the winner!")
            else:
                print(f"You lost the game. Winner is the {winning_color}")

        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)



screen.exitonclick()
