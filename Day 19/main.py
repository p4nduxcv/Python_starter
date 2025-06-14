from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# this is a Eventlistner
def move_forward():
    tim.forward(10)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_backward():
    tim.backward(10)

def clean():
    tim.clear()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(move_backward,"s")
screen.onkey(clean,"c")
screen.exitonclick()


