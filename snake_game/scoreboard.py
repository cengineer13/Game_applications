from turtle import Turtle
ALIGMENT = "center"
FONT =("Calibri", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(f"Score:  {self.score}", align="center", font=("Calibri", 18, "normal"))

    def update_score(self):
        self.write(f"Score:  {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self,):
        self.score += 1
        self.clear()
        self.update_score()

    def game_finish(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGMENT, font=FONT)








