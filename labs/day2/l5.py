import turtle
import numpy as np

k = 0.3

turtle.speed(0)
turtle.tracer(False)

def draw(a):
    turtle.left(a)

    turtle.penup()
    turtle.forward(k*a)
    turtle.pendown()
    turtle.forward(1)
    turtle.forward(-1)
    turtle.penup()
    turtle.backward(k*a)

    turtle.left(-a)

for phi in np.arange(0,360*10,0.3):
    draw(phi)

turtle.exitonclick()