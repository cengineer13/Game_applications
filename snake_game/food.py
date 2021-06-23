from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.refresh()

    def refresh(self):
        random_x =random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)