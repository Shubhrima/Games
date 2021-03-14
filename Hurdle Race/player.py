from turtle import Turtle

START_POS=(0,-280)
DIST=10
END_POS=(0,280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.setpos(START_POS)

    def move_up(self):
        self.forward(DIST)

    def begin(self):
        self.penup()
        self.goto(START_POS)