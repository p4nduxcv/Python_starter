from turtle import Turtle

XCOR = 350
Y_UPPER_LIMIT = 240
Y_LOWER_LIMIT = -240

class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(positions)

    def go_up(self):
        if Y_UPPER_LIMIT > self.ycor():
            new_y = self.ycor() + 20
            self.goto(XCOR, new_y)

    def go_down(self):
        if Y_LOWER_LIMIT < self.ycor():
            new_y = self.ycor() - 20
            self.goto(XCOR, new_y)





