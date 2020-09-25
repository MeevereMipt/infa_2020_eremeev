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
step = 10

turtle.tracer(False)

turtle.penup()
for r in range(50,n*step+51, step):
    turtle.forward(r)
    drawCircle(r)
    turtle.forward(-2*r)
    drawCircle(r)
    turtle.forward(r)

turtle.exitonclick()


