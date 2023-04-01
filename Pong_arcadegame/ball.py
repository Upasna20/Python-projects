from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.home()
        self.X_STRIDE = 10
        self.Y_STRIDE = -10
        self.r_score = 0
        self.l_score = 0
        self.ballspeed = 0.1

    def move(self):
        new_y = self.ycor() + self.Y_STRIDE
        new_x = self.xcor() + self.X_STRIDE
        self.goto(new_x, new_y)

    def bounce(self):
        self.Y_STRIDE *= -1

    def paddlebounce(self):
        self.X_STRIDE *= -1
        self.ballspeed *= 0.75


    def reset(self):
        if self.xcor() > 0:
            self.X_STRIDE = - abs(self.X_STRIDE)
            # print(self.X_STRIDE)
            self.Y_STRIDE = - abs(self.Y_STRIDE)
            # print(self.Y_STRIDE)
            self.goto(0, 0)
            self.l_score += 1
        else:
            self.X_STRIDE = abs(self.X_STRIDE)
            self.Y_STRIDE = - abs(self.Y_STRIDE)
            self.goto(0, 0)
            self.r_score += 1
        self.ballspeed = 0.1