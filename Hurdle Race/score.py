FONT=('Courier',25, 'normal')
LEVEL=1

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=LEVEL
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.color('black')
        self.write("Level: " + str(self.level), align="center", font=("Courrier", 10, "normal"))
    def end(self):
        self.goto(0, 0)
        self.color('black')
        self.write("GAME OVER", align="center", font=("Courrier", 55, "bold"))

    def level_up(self):
        self.level+=1
        self.clear()
        self.goto(-270, 270)
        self.color('black')
        self.write("Level: "+str(self.level), align="center", font=("Courrier", 10, "normal"))


