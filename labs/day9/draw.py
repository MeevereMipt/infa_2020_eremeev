import turtle as t

tl = t.Turtle()
stack = []
angle = 30
distance = 0.5

t.tracer(0,0)

def draw(string : str, rules):

    tl.setheading(90)
    for sym in string:
        rules[sym]()


def left_bracket_rule():
    stack.append((
        tl.position(),
        tl.heading()
    ))
    tl.left(angle)


def plus_rule():
    tl.right(angle)


def right_bracket_rule():
    params = stack.pop()
    tl.penup()
    tl.setposition(*params[0])
    tl.pendown()
    tl.setheading(params[1])
    tl.right(angle)


def minus_rule():
    tl.left(angle)


def one_rule():
    tl.forward(distance)

def zero_rule():
    tl.forward(3)
