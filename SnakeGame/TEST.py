from turtle import Turtle
import time

class Test(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.setpos((30, 40))
        self.penup()


tim = Test()
time.sleep(1)
tim = Test()
tim.goto(60, 80)
tim.color('pink')
# if int(input('number?')) > 3:
#     tim = Test()
#     tim.color('pink')
