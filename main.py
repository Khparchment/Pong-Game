from turtle import Screen
from paddle import Paddle
from net import Net
from ball import Ball
from scoreboard import Scoreboard
import time

#create screen for came
screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()



#create paddles for playing and create a ball object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()






x=0
y=-300

for _ in range(1,22):
    net = Net()
    net.goto(x, y)
    y += 30



screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    if ball.xcor() > 350:
        ball.reset_ball()
    if ball.xcor() < -350:
        ball.reset_ball()

































screen.exitonclick()