import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500,600)
user_bet = screen.textinput("Make your bet", "Which turtle will win the game ?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    turtles.append(tim)


for i in range(0, len(turtles)):
    turtles[i].penup()
    turtles[i].goto(-250,-200 + i*100)


screen.exitonclick()


