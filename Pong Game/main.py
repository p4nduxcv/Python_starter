from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
is_game_one = True

while is_game_one:
    screen.update()
    screen.listen()

    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")




screen.exitonclick()