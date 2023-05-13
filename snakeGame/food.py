import random
from turtle import Turtle, Screen
import time

#
# POS = range(-290, 290)
# screen = Screen()
# screen.tracer(0)
# screen.bgcolor('black')
# class Food:
#     def create_food(self):
#         food = Turtle(shape='circle')
#         food.color('white')
#         food.penup()
#         food.setpos(random.choices(POS, k=2))
#         screen.update()
#         time.sleep(0.2)
'''do you see here why we went for inheritance as an option because all the attributes and properties that we are using 
is nothing but everything related to the turtle and the food class in itself has no uniqueness.'''


#
# while True:
#     food = Food()
#     food.create_food()

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.refresh()
        self.penup()

    def refresh(self):
        position = random.choices((-240, 250), k=2)
        self.goto(position)
