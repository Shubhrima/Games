from turtle import Turtle

class Bar(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed(10)
        self.shapesize(stretch_wid=1.0, stretch_len=5, outline=None)
        self.penup()
        self.right(90)
        self.goto(position)

    def move_up(self):
        y_pos= self.ycor()+20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos= self.ycor()-20
        self.goto(self.xcor(), y_pos)



