from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.penup()
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_paddle_score, align="center", font=("Cambria", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_paddle_score, align="center", font=("Cambria", 70, "normal"))

    def l_point(self):
        self.l_paddle_score +=1
        self.update_score()

    def r_point(self):
        self.r_paddle_score +=1
        self.update_score()
