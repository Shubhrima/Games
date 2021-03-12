from turtle import Turtle
import random

MOVE_DISTANCE=25

snake=Turtle()
snake.shape('square')
snake.color('white')
snake.speed(10)
snake.shapesize(stretch_wid=.5, stretch_len=1.5, outline=None)

def up():
    if snake.heading() != 270:
        '''up to down not allowed'''
        snake.penup()
        snake.setheading(90)
        snake.forward(MOVE_DISTANCE)

def down():
    if snake.heading() != 90:
        snake.penup()
        snake.setheading(270)
        snake.forward(MOVE_DISTANCE)

def left():
    if snake.heading() != 0:
        '''left to right not allowed'''
        snake.penup()
        snake.setheading(180)
        snake.forward(MOVE_DISTANCE)

def right():
    if snake.heading()!=180:
        snake.penup()
        snake.setheading(0)
        snake.forward(MOVE_DISTANCE)





