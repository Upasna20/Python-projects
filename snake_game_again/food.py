from turtle import Turtle, Screen
import random


screen = Screen()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        """did you see how the Turtle doesn't actually get created if we do not mention the super() function to 
        invoke the Turtle class, this is because even though Turtle is the parent class but it's init method will
        not get executed if we already have an init method in the Food sub class. If we want to have certain 
        special features in the food class that takes the Turtle class but also adds its own features then we
        must use the super() method."""

        self.shape("circle")
        self.color("green")
        self.shapesize(0.7, 0.7, 0.7)
        self.bait_move()
        # print(self.pos())
    def bait_move(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)







