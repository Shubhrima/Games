import time
import random
from turtle import Screen
from score import Score
from cars import Car
from player import Player

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.move_up, "Up")

game_on=True
cars=Car()
score=Score()

while game_on:
    time.sleep(0.1)
    if player.ycor() >= 280:
        player.begin()
        cars.speed_up()
        score.level_up()

    for car in cars.all_cars:
        if car.distance(player)<=20:
            score.end()
            game_on=False


    carproduce=random.randint(1,5)
    if carproduce==5:
        cars.create_car()
    cars.move()

    screen.update()


screen.exitonclick()
