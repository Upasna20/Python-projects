from turtle import Turtle, Screen

screen = Screen()
with open("data.txt") as file:
    num = int(file.read())

ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = num
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.update()
        '''This command writes the argument then and there itself and it is kind of like the
        print command for the console. So, it is like the same for the graphic screen. '''

    def update(self):
        self.clear()
        self.write(f'Score:{self.score}, High_score: {self.high_score}', align=ALIGNMENT, font=FONT)
        screen.update()

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
        '''So, we print the write command everytime the snake hits the food. But, we also need to clear
         the previous written texts so we put in the clear command.'''

    def gameover(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def check(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # num = self.high_score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update()
