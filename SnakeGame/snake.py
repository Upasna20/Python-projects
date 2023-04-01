from turtle import Screen
from turtle import Turtle
import time

MOVE_DISTANCE = 20

screen = Screen()
screen.bgcolor('black')


class Snake:

    def __init__(self):
        self.segment = None
        self.segments = []
        self.pos = [(40, 0), (20, 0), (0, 0)]

        self.screen = Screen()
        # screen.tracer(0)

    def Right(self):
        direction = self.segments[0].heading()
        if direction == 90:
            self.segments[0].right(90)

        elif direction == 270:
            self.segments[0].left(90)

    def Left(self):
        direction = self.segments[0].heading()
        if direction == 90:
            self.segments[0].left(90)

        elif direction == 270:
            self.segments[0].right(90)

    def Up(self):
        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].left(90)

        elif direction == 180:
            self.segments[0].right(90)

    def Down(self):

        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].right(90)

        elif direction == 180:
            self.segments[0].left(90)

    def create_snake(self):
        for i in self.pos:
            self.segment = Turtle(shape='square')
            self.segment.penup()
            self.segment.speed('slowest')
            self.segment.color('white')
            self.segment.setpos(i)
            # time.sleep(1)
            self.segments.append(self.segment)
            # time.sleep(1)
        self.segments[1].color('orange')
        # time.sleep(1)
        self.segments[2].color('green')
        # time.sleep(1)
        # print(self.segments)
        screen.update()

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            # time.sleep(1)
            # screen.update()
            ''' well we used update to show the snap of the movement of the turtle at the exact time when the second
             block has eclipsed the first block. '''
            # time.sleep(1)
            '''This time sleep command commands the computer to move to the next command of shifting the first block 
            forward slowly so that the user is not rushed to see the first block move forward but the user gets 
            enough time to see the first block eclipsed otherwise since these computers are so fast even though the 
            eclipsed part has been made available for showcasing, since the non eclipsed is made available too, the 
            screen would have to show both and thus the screen would not stay at the eclipsed portion for long 
            enough for human eyes to detect and since time sleep has to be initiated after forward movement 
            otherwise we would only see a line not a snake in the terminal so all this automatically favors the non
            eclipsed portion to stay visible for longer because the sleep command stops the processor from moving 
            further and thus we would only see the non eclipsed version as the eclipsed would be too quick to 
            disappear. However, if we add a time sleep option not just after the forward command but also after the
            eclipsed appearance update command then it would mean we are instructing the compiler to stop moving 
            further and wait at the eclipsed command for sometime this means we get a squiggly motion.'''
        self.segments[0].forward(MOVE_DISTANCE)
        screen.update()#tweak done here as well.
        # time.sleep(0.1) #(tweak done here if not on the main side of the snake object.)
        # THE PRESENCE OF THIS GIVES THE SQUIGGLY MOVEMENT
        #      function to check movement and then redirecting to a function that turns it left
        # screen.update()
        # time.sleep(1)
        '''Now, as far as turning at the right time is concerned it depends on at what stage of snake movement is
         the key pressed. Through observation, we can say that if the key is pressed when the orange block has just
        eclipsed the first bl0ck then if the key is pressed at that moment then the computer prioritizes completing 
        a straight forward movement and then turning that same block so the actual right movement actually happens 
        one movement cycle after the key is pressed . This might happen in the case where the second block eclipses 
        the first block and the user gets enough time to hit the key at that very moment . Well, this is only 
        possible if that stage is shown and enough time is given to the user before the command moves to the next
        command. and this is made possible via the time sleep command.At any other possible orientation of the snake
        block movement, if the key is pressed the result are instantaneous. The second time when we stop the command
        from proceeding forth is when the first block just moves forward and in that case if the key is hit, the 
        turn is instantaneous.'''
    def new_part(self):
        position = self.segments[-1].position()
        # print(position)
        self.segment = Turtle()
        self.segment = Turtle(shape='square')
        self.segment.penup()
        self.segment.speed('slowest')
        self.segment.color('white')
        self.segment.setpos(position)
        # time.sleep(1)
        self.segments.append(self.segment)

    def goto(self):
        for segment in self.segments:
            segment.goto(1000, 1000)


    def new_snake(self):
        self.segments = []
        self.create_snake()

