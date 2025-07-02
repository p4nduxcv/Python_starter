from turtle import Turtle

XCOR = 350
Y_UPPER_LIMIT = 240
Y_LOWER_LIMIT = -240

class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(XCOR, 0)

    def go_up(self):
        if Y_UPPER_LIMIT > self.paddle.ycor():
            new_y = self.paddle.ycor() + 20
            self.paddle.goto(XCOR, new_y)

    def go_down(self):
        if Y_LOWER_LIMIT < self.paddle.ycor():
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(XCOR, new_y)





