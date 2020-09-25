from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 100

turtle.tracer(1,0)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(randint(-5,7))
        unit.left(randint(-180,180))