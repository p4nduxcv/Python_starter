from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# this is a Eventlistner
def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()


