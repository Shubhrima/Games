
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.mark=-1
        self.goto(0, 280)
        self.hideturtle()
        self.increase_score()


    def increase_score(self):
        self.mark+=1
        self.clear()
        self.write("Score = "+str(self.mark), align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courrier", 55, "bold"))