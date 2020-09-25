import turtle as t

LENGTH = (20,20)

REFERENCE = {}
with open("reference.txt") as file:
    for line in file:
        dec1 = line.split(":")

        digit = int(dec1[0])
        tupl = eval(dec1[1])
        REFERENCE[digit] = tupl

def drawdigit(a):
    tupl = REFERENCE[a]
    pos = t.pos()
    for elem in tupl:
        t.penup()
        if(elem[2] == 1):
            t.pendown()
        t.goto(elem[0]*LENGTH[0]+pos[0], -(elem[1]*LENGTH[1])+pos[1])

def drawnumber(ls, offset=(0,0)):
    for i in range(0,len(ls)):
        t.penup()
        t.goto(1.5*i*LENGTH[0] - offset[0], 0 - offset[1])
        drawdigit(ls[i])

drawnumber([1,4,1,7,0,0],(50,0))

t.exitonclick()