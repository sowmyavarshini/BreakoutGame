from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1050, height=600)
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
score = Score()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')


def collision_with_walls():
    global ball, game_on
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    if ball.xcor() > 500 or ball.xcor() < -500:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.ycor() < -300:
        score.lives -= 1
        score.update_score()
        if score.lives == 0:
            score.game_status(win=False)
            game_on = False
        else:
            ball.reset_position()
        return


def collision_with_paddle():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()
    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def collision_with_bricks():
    global ball, bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.goto(2000, 2000)
                bricks.bricks.remove(brick)
                score.point(brick)
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    collision_with_walls()

    collision_with_paddle()

    collision_with_bricks()

    if len(bricks.bricks) == 0:
        score.game_status(win=True)
        break


screen.exitonclick()
