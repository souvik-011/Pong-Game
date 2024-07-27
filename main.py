from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scorecard import Scorecard

scene = Screen()
scene.setup(800, 600)
scene.bgcolor("black")
scene.title("Pong Game")
scene.tracer(0)

r_paddle = Paddle(380, 0)
l_paddle = Paddle(-380, 0)

ball = Ball()

scorecard = Scorecard()

# tur = Turtle()
# tur.color("white")
# tur.goto(330,-300)
# tur.goto(330,300)
# print(tur.xcor())

scene.listen()
scene.onkey(r_paddle.go_up, "Up")
scene.onkey(r_paddle.go_down, "Down")
scene.onkey(l_paddle.go_up, "w")
scene.onkey(l_paddle.go_down, "s")

is_true = True

while is_true:

    time.sleep(0.1)
    scene.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.setx(350)
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.setx(-350)
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.bounce_x()
        scorecard.l_point()

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.bounce_x()
        scorecard.r_point()


scene.exitonclick()
