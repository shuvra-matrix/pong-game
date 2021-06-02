from turtle import Screen
from padel import Padel
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("PONG GAME")
LEVEL = screen.textinput(title="Choose Your Game Level", prompt=" EASY = E , NORMAL = N , HARD = H").lower()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

tim = Padel((350, 0))
tim_2 = Padel((-350, 0))
ball = Ball()
score = Score()
screen.listen()

screen.onkey(fun=tim_2.up, key="w")
screen.onkey(fun=tim_2.down, key="s")
screen.onkey(fun=tim_2.up, key="W")
screen.onkey(fun=tim_2.down, key="S")
screen.onkey(fun=tim.up, key="Up")
screen.onkey(fun=tim.down, key="Down")
speed = ball.ball_speed(LEVEL=LEVEL)

game_is_not_finished = True

while game_is_not_finished:
    time.sleep(speed)
    screen.update()
    ball.ball_move()
    if score.right_score == 10 and LEVEL == 'e' or score.left_score == 10 and LEVEL == 'e':
        game_is_not_finished = False
        score.game_over()
    if score.right_score == 15 and LEVEL == 'n' or score.left_score == 15 and LEVEL == 'n':
        game_is_not_finished = False
        score.game_over()
    if score.right_score == 20 and LEVEL == 'h' or score.left_score == 20 and LEVEL == 'h':
        game_is_not_finished = False
        score.game_over()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_jump()

    if ball.distance(tim) < 50 and ball.xcor() > 320 or ball.distance(tim_2) < 50 and ball.xcor() < -320:
        ball.ball_new_bounce()
        speed = speed * 0.9

    if ball.xcor() > 410:
        ball.new_position()
        score.left_score_increase()
        speed = ball.ball_speed(LEVEL=LEVEL)
    if ball.xcor() < -410:
        ball.new_position()
        score.right_score_increase()
        speed = ball.ball_speed(LEVEL=LEVEL)

screen.exitonclick()
