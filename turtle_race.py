"""Etch-a-sketch app using turtle package"""

from turtle import Turtle , Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clear_screen():
    tim.home()
    tim.clear()

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()