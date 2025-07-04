from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
is_game_one = True

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while is_game_one:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()






screen.exitonclick()