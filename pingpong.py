from turtle import Screen
from paddle import paddle as pd
from ball import Ball as bl
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = pd(350, 0)
paddle2 = pd(-350, 0)
ball = bl(12, -20)

screen.listen()
(screen.onkey(paddle1.go_up, "Up"))
(screen.onkey(paddle1.go_down, "Down"))
(screen.onkey(paddle2.go_down, "s"))
(screen.onkey(paddle2.go_up, "w")) 


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
    #ball needs to bounce
       ball.bounce()








screen.exitonclick()

