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


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()
