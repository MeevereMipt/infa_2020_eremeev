import turtle
from random import *

t = turtle.Turtle()

running = True
def stopRun(a,b) -> None:
    global running
    print("test")
    running = False
    
t.onclick(stopRun)

while running:
    t.forward(randint(2,20))
    t.left(randint(-180,180))

