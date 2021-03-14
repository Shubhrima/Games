colours=['red','blue','green','yellow','aqua','orange', 'pink', 'violet','brown','indigo','purple']
START=5
INCREASE=2


from turtle import Turtle
import random
cars=[]

class Car():
    def __init__(self):
        self.all_cars=[]
        self.speed = START

    def create_car(self):
        new_car=Turtle('square')
        random_integer = random.randint(0, 9)
        new_car.color(colours[random_integer])
        new_car.shapesize(stretch_wid=1.0, stretch_len=3, outline=None)
        new_car.penup()
        random_y = random.randint(-250, 250)
        random_x = random.randint(280,320)
        new_car.setpos(random_x, random_y)
        self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
                car.backward(self.speed)

    def car_begin(self):
        self.penup()
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)

    def speed_up(self):
        self.speed+=INCREASE


