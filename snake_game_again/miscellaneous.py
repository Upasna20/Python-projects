from turtle import Turtle

with open("data.txt", mode="r+") as score_sheet:
    score_sheet.seek(0)
    max_score = score_sheet.read()



class text(Turtle):
    def __init__(self, color="white", goto=(0, 270)):
        super().__init__()
        self.ht()
        self.penup()
        self.color(color)
        self.goto(goto[0], goto[1])

    def text_write(self, text, Align, size=8):
        self.write(arg=text, align=Align, font=("Arial", size, "normal"))

    def text_invisible(self):
        self.clear()


class Score:
    def __init__(self):
        self.score = 0
        self.text_object = []

    def score_increase(self):
        self.score += 1


    def score_read(self):
        with open("data.txt", mode="r") as score_sheet:
            read_score = score_sheet.read()
        if self.text_object:
            self.text_object[-1].text_invisible()
        score_heading = text(goto=(-150, 270))
        max_score_heading = text(goto=(150, 270))
        self.text_object.append(score_heading)
        max_score_heading.text_write(text=f"High Score : {read_score}", Align="left", size=12)
        score_heading.text_write(text=f"Current Score : {self.score}", Align="right", size=12)

    def game_ends(self):
        if self.score > int(max_score):
            with open('data.txt', "w") as file:
                file.write(f"{self.score}")

        gameover = text(goto=(0, 0))
        gameover.text_write("Gameover!!!", Align="center", size=40)

