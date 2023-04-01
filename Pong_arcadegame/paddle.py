from turtle import Turtle
ONE_STRIDE = 10


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.setheading(90)
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(pos)
        self.color('white')

    def Up(self):
        self.fd(ONE_STRIDE)

    def Down(self):
        self.back(ONE_STRIDE)
