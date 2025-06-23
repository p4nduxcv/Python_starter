import time
from turtle import Turtle, Screen
from snake import Snake

snake = Snake()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("MSG")

screen.tracer(0)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move()



screen.exitonclick()
