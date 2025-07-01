from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  #0, 1, 2
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start=2, stop=0, step=-1
            new_x = self.segments[seg_num - 1].xcor()  # -20, 1 | 0,0
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
            # self.head.left(90)

    def up(self):
        if self.head.setheading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)

