from turtle import Turtle


class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350, 0)





