from turtle import Turtle, Screen
import random

won=""
race_on= False

screen=Screen()
screen.bgcolor("black")
screen.setup(width=500,height=500)
screen.title('Turtle Betting')
guess=screen.textinput("Racing Betting", "Who do you think will win:")



colors=["white","blue", "green","yellow", "orange", "red"]
yposition=[-150, -90, -30, 30, 90, 150]
turtles=[]

for t in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=yposition[t])
    turtles.append(new_turtle)


if guess:
    race_on=True

while(race_on):
    for t in turtles:
        dist= random.randint(0,10)
        t.forward(dist)
        if t.xcor()>=230:
            race_on=False
            won=t.pencolor()

if won==guess:
    print("You won the bet.")
else:
    print("You lose, "+guess+" did not win. Turtle " +won+" won the game.")





screen.exitonclick()