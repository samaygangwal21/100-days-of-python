from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']
y = -100
all_turtles = []

for c in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(c)          # set the turtle's color
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for s in all_turtles:
        if s.xcor() > 230:
            winner = s.pencolor()
            is_race_on = False
            break
        s.forward(random.randint(5,15))

if winner == user_bet.lower():
    print(f"You Won! The winner was {winner}")
else:
    print(f"You Lost! The winner was {winner}")

screen.bye()
