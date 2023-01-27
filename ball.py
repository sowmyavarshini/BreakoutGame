from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('grey')
        self.penup()
        self.goto(x=-20, y=-200)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce or (self.ycor() == 136 or self.ycor() == 170):
            self.x_move *= -1
            self.move_speed *= 0.9
        if y_bounce:
            self.y_move *= -1

    def reset_position(self):
        self.goto(x=-20, y=-200)
        self.y_move = 10
        self.move_speed = 0.1
