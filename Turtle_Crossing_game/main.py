import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(player.go_up, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line
    if player.ycor() > 280 :
        player.restart()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
