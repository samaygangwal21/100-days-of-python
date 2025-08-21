import turtle
import pandas

data = pandas.read_csv("28_states.csv")
screen = turtle.Screen()
screen.title("India State Game")
screen.setup(width=682, height=800)
image = "india_map.gif"
screen.bgpic(image)
data_states = data["state"].to_list()

quit1 = turtle.Turtle()
quit1.hideturtle()
quit1.penup()
quit1.goto(240, 350)
quit1.write("Enter 'Exit' to Quit")


while len(data_states) > 0:
    answer_state = screen.textinput(title=f"India Quiz {36 - len(data_states)}/36",
                                    prompt="Guess the State/UT:" ).strip().title()
    if answer_state in data_states:
        data_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

    if answer_state == "Exit":
        new_data = pandas.DataFrame(data_states)
        new_data.to_csv("States/Ut_to_learn.csv")
        break

if len(data_states) == 0 :
    e = turtle.Turtle()
    e.hideturtle()
    e.penup()
    e.write("Congrats! You have guessed it all", align="center", font=("Arial", 24, "bold"))




screen.exitonclick()