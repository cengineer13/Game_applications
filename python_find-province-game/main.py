import turtle
import pandas
screen = turtle.Screen()
image = "map_of_uzbekistan.gif"
turtle.addshape(image)
turtle.shape(image)

correct_answers = []


data = pandas.read_csv("viloyatlar.csv")
all_provinces = data["viloyat"].tolist()

while len(correct_answers) < 13:
    answer_state = screen.textinput(title=f"Viloyatni toping {len(correct_answers)}/13", prompt="Viloyat nomini yozing. (Lotincha)").title()

    if answer_state == "Chiqish":
        should_learn = [province for province in all_provinces if province not in correct_answers]
        df = pandas.DataFrame(should_learn, columns=["Viloyatlar"])
        df.to_csv("O'rganib oling!", index=False)
        break

    if answer_state in all_provinces:
        correct_answers.append(answer_state)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        current_province = data[data["viloyat"] == answer_state]
        t.goto(int(current_province.x), int(current_province.y))
        t.write(answer_state)



