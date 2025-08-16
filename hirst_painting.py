import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(202, 164, 110),(236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
for j in range(1,100):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(40)
    if j % 10 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)
tim.dot(20, random.choice(color_list))

screen = turtle_module.Screen()
screen.exitonclick()