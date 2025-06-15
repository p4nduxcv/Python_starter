import random
from turtle import Turtle, Screen


is_race_start = False
screen = Screen()
screen.setup(500,600)
user_bet = screen.textinput("Make your bet", "Which turtle will win the game ?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    turtles.append(tim)
    turtles[i].penup()
    turtles[i].goto(-250,-200 + i*100)

if user_bet:
    is_race_start = True

while is_race_start:
    for i in range(len(turtles)):
        if turtles[i].xcor() > 280:
            is_race_start = False
            winning_color = turtles[i].pencolor()
            if winning_color == user_bet:
                print("You Won")
            else:
                print(f"{winning_color} is won")
        turtles[i].forward(random.randint(0,10))



screen.exitonclick()


