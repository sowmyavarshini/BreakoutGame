from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('Blue')
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(x=0, y=-250)

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())
