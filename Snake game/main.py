import snake
from food import Food
from turtle import Screen
import time
from score import Score

game_on=True
x=1.5
food =Food()
score= Score()

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')

screen.listen()

def snake_move():
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.down, key="Down")

while game_on:
    time.sleep(0.1)
    screen.update()
    if game_on==True:
        snake_move()

    if snake.snake.distance(food)<=15:
        food.refresh()
        snake.snake.resizemode("user")
        x+=0.5
        snake.snake.shapesize(stretch_len=x)
        score.increase_score()

    if x==snake.snake.xcor():
        snake.snake.color('red')
        score.game_over()
        game_on = False

    if snake.snake.xcor() >= 275 or snake.snake.xcor()<=-275 or snake.snake.ycor()>=275 or snake.snake.ycor()<=-275:
       snake.snake.color('red')
       score.game_over()
       game_on = False


screen.exitonclick()