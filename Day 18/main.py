from turtle import Turtle, Screen
import random
from colors import ColorsList

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(2)
timmy_the_turtle.width(5)

dir = [0, 90, 180, 270]

def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

for _ in range(200):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(random.choice(dir))
    timmy_the_turtle.pencolor(get_random_color())


timmy_the_turtle_screen = Screen()
timmy_the_turtle_screen.exitonclick()



