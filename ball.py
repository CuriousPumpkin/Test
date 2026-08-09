from turtle import Turtle

class Ball(Turtle):
    def __init__(self,xmove,ymove):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.xmove = xmove
        self.ymove = ymove
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def y_bounce(self):
       self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)