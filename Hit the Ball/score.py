
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.mark_left=-1
        self.mark_right = -1
        self.increase_score_right()
        self.increase_score_left()
        self.hideturtle()

    def update_score(self):
        self.goto(-100, 250)
        self.write(str(self.mark_left), align="center", font=("Arial", 35, "normal"))
        self.goto(100, 250)
        self.write(str(self.mark_right), align="center", font=("Arial", 35, "normal"))



    def increase_score_left(self):
        self.mark_left+=1
        self.clear()
        self.update_score()


    def increase_score_right(self):
        self.mark_right+=1
        self.clear()
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME ENDED", align="center", font=("Courrier", 55, "bold"))