from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MSG")

segment_positions = [(0,0),(-20,0),(-40,0)]

for position in segment_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("yellow")
    new_segment.goto(position)


screen.exitonclick()