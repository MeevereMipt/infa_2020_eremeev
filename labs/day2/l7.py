import turtle
import math

def drawPolygon(R,n):

    turtle.up()
    turtle.forward(R)
    turtle.left(90)

    a = 2 * R * math.sin( math.pi / n )
    turtle.down()
    turtle.forward(a/2)
    turtle.left(360 / n)
    for i in range(2,n+1):
        turtle.forward(a)
        turtle.left(360 / n)
    turtle.forward(a / 2)
    turtle.up()

    turtle.right(90)
    turtle.forward(-R)

def drawCircle(R):
    drawPolygon(R, 50)

n = 10
R = 50
turtle.up()

turtle.speed(0)
turtle.tracer(False)

for i in range(0,n):
    turtle.forward(R)
    drawCircle(R)
    turtle.forward(-R)
    turtle.left(360/n)

turtle.exitonclick()