from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score_display()

    def update_score_display(self):
        self.clear()  # Clear the previous score text
        self.write(f"Score : {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def scorecard(self):
        self.score += 1
        self.update_score_display()