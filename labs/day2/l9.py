import turtle
import math

def drawPolygon(R,n,phi):
    heading = turtle.heading()

    turtle.up()
    turtle.forward(R)
    turtle.left(90)

    a = 2 * R * math.sin( math.pi / n )
    turtle.down()
    turtle.forward(a/2)
    turtle.left(360 / n)
    for i in range(2, phi*n//360 +1):
        turtle.forward(a)
        turtle.left(360 / n)
    turtle.forward(a / 2)
    turtle.up()

    turtle.right(90)
    turtle.forward(-R)

    turtle.seth(heading)

turtle.speed(0)


for i in range(1,5):
    drawPolygon(50,150,180)
    turtle.forward(40)
    turtle.left(180)
    drawPolygon(10, 150, 180)
    turtle.left(180)
    turtle.forward(40)

turtle.exitonclick()