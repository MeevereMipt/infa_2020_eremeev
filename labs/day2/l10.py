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

def drawCircle(R):
    drawPolygon(R,170,360)

# turtle.tracer(False)

turtle.color("black", "yellow")
turtle.begin_fill()
drawCircle(100)
turtle.end_fill()

turtle.goto(40,40)
turtle.color("black", "blue")
turtle.begin_fill()
drawCircle(20)
turtle.end_fill()

turtle.goto(-40,40)
turtle.color("black", "blue")
turtle.begin_fill()
drawCircle(20)
turtle.end_fill()

turtle.goto(0,30)
turtle.seth(270)

turtle.pensize(4)
turtle.pendown()
turtle.forward(30)


turtle.goto(0,0)
turtle.right(90)
turtle.color("red", "red")
drawPolygon(40, 150, 180)


turtle.exitonclick()
