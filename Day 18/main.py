from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(2)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def draw_shape(leg_count):
    angle = 360/leg_count
    for _ in range(leg_count):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(angle)


#Squar
for num_of_legs in range(3, 10):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(num_of_legs)



timmy_the_turtle_screen = Screen()
timmy_the_turtle_screen.exitonclick()



