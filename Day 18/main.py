from turtle import Turtle, Screen
import random
from colors import ColorsList

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(2)
timmy_the_turtle.width(5)


dir = [0, 90, 180, 270]

for _ in range(200):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(random.choice(dir))
    timmy_the_turtle.color(random.choice(ColorsList))


timmy_the_turtle_screen = Screen()
timmy_the_turtle_screen.exitonclick()



