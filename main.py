import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_answer = []

play = 3

while play:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 Correct answers",
                                    prompt="What's another state's name?").title()
    if answer_state in states:
        if answer_state not in correct_answer:
            correct_answer.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x_cor = data[data.state == answer_state].x
            y_cor = data[data.state == answer_state].y
            t.goto(int(x_cor), int(y_cor))
            t.write(answer_state)
    else:
        play -= 1

for state in states:
    if state not in correct_answer:
        t = turtle.Turtle()
        t.color("red")
        t.hideturtle()
        t.penup()
        x_cor = data[data.state == state].x
        y_cor = data[data.state == state].y
        t.goto(int(x_cor), int(y_cor))
        t.write(state)


screen.exitonclick()
