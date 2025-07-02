from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
paddle = Paddle()
is_game_one = True

while is_game_one:
    screen.update()
    screen.listen()

    screen.onkey(paddle.go_up, "Up")
    screen.onkey(paddle.go_down, "Down")




screen.exitonclick()