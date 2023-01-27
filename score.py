from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=100, y=230)
        self.write(f'Lives:{self.lives}   {self.score}', align='center', font=('Courier', 30, 'normal'))

    def point(self, brick):
        if brick.color() == ('red', 'red') or brick.color() == ('orange', 'orange'):
            self.score += 7
        else:
            self.score += 4
        self.update_score()

    def game_status(self, win):
        self.clear()
        if win:
            self.write('Game win', align='center', font=('Courier', 50, 'normal'))
        else:
            self.write('Game Over', align='center', font=('Courier', 50, 'normal'))



