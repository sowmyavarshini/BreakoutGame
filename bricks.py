from turtle import Turtle
COLORS = ['green', 'yellow', 'orange', 'red']
points = {
    'green': 4,
    'yellow': 4,
    'orange': 7,
    'red': 7
}


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=4, stretch_wid=1.5)
        self.penup()
        self.quantity = 1
        if y_cor == 0 or y_cor == 34:
            self.color('green')
        elif y_cor == 68 or y_cor == 102:
            self.color('yellow')
        elif y_cor == 136:
            self.color('orange')
        else:
            self.color('red')
        self.goto(x=x_cor, y=y_cor)

        self.left_wall = self.xcor() - 40
        self.right_wall = self.xcor() + 40
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 180
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-480, 480, 85):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 34):
            self.create_lane(i)

