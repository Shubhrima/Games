from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.speed(5)
        self.penup()
        self.y_move=3
        self.x_move=3

    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)

    def bounce_y(self):
        self.y_move = self.y_move *-1

    def bounce_x(self):
        self.x_move = self.x_move *-1

    def reset_ball(self,position):
        self.goto(position)
        self.bounce_x()