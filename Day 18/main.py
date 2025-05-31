from turtle import Turtle, Screen
import random
from colors import ColorsList

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed("fastest")

screen = Screen()
screen.colormode(255)

def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(get_random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)
        print(timmy_the_turtle.heading())


draw_spirograph(1)




screen.exitonclick()



