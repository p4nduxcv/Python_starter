import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start_line()
        car_manager.level_up()
        scoreboard.update_levels()







screen.exitonclick()