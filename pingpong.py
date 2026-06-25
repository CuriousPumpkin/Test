from turtle import Screen
from paddle import paddle as pd

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)

paddle1 = pd(350, 0)
paddle2 = pd(-350, 0)
# ball = PingPong()





screen.exitonclick()

