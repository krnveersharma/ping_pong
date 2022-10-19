from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scroreboard import Score
import time
score=Score()
screen=Screen()
screen.setup(800,700)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)
game_is_on=True
r_paddle=Paddle(370,0)
l_paddle=Paddle(-370,0)
ball = Ball()
# moving of paddle
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>330 or ball.ycor()<-330:
        ball.bounce()
    if ball.distance(r_paddle)<50 and ball.xcor()>350:
        ball.paddle_bounce()
        score.r_update_score()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.paddle_bounce()
        score.l_update_score()
    if ball.xcor()>370:
        ball.reset_pos()
        score.reset()
    if ball.xcor() < -370:
        ball.reset_pos()
        score.reset()




























screen.exitonclick()
