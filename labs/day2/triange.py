import turtle

def drawTriangle(pos, a, t):
    t.goto(pos)
    t.up()
    t.right(30)
    t.forward(a/(3**(0.5)))
    t.left(150)

    t.down()
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.right(30)

    t.up()
    t.forward(-a / (3 ** (0.5)))
    t.left(30)

def frac(iter, R):
    pass

t1 = turtle.Turtle()
drawTriangle((0,0),100, t1)

