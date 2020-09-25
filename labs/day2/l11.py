import turtle
import math

def drawStar(R,n):
    heading = turtle.heading()

    turtle.up()
    turtle.forward(R)
    turtle.left(90)

    a = 2 * R * math.sin( math.pi / n )
    turtle.down()

    for i in range(0, n):
        turtle.forward(a)
        turtle.left(360 * ((2*(n//2) +3)//2 ) / n)
    turtle.up()

    turtle.right(90)
    turtle.forward(-R)

    turtle.seth(heading)

drawStar(100,5)