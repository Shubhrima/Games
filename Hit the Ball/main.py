from turtle import Screen
from bars import Bar
from ball import Ball
from score import Score


lbar=Bar((-350,0))
rbar=Bar((350,0))
ball=Ball()
score=Score()

screen=Screen()
screen.setup(800,600)
screen.title('Pong game')
screen.bgcolor('black')

screen=Screen()
screen.listen()
screen.onkey(fun=rbar.move_up, key="Up")
screen.onkey(fun=rbar.move_down, key="Down")

screen.onkey(fun=lbar.move_up, key="z")
screen.onkey(fun=lbar.move_down, key="x")

game_on=True
while game_on:
    ball.move()
    ball.color('yellow')
    '''hits top and bottom edges'''
    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bounce_y()

    '''hits bars'''
    if ball.distance(rbar)<50 and ball.xcor()>325:
        ball.color('green')
        ball.bounce_x()
        score.increase_score_right()

    if ball.distance(lbar)<50 and ball.xcor()<-325:
        ball.color('green')
        ball.bounce_x()
        score.increase_score_left()


    #restart
    if ball.xcor()>385:
        ball.reset_ball((150,-275))
    if ball.xcor()<-385:
        ball.reset_ball((-150,-275))

    #end
    if score.mark_right==10 or score.mark_left==10:
        score.game_over()
        game_on=False


screen.exitonclick()