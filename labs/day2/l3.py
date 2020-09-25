import turtle 

def drawRect(a : int):
    turtle.penup()
    turtle.forward(a/2)
    turtle.left(90)

    turtle.pendown()
    turtle.forward(a/2)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a/2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(a/2)

for a in range(100,200,10):
    drawRect(a)
