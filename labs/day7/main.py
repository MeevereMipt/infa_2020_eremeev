from random import randrange as rnd, choice
import tkinter as tk
import math
import time

from labs.day7.Ball import Ball, checkBalls
from labs.day7.Gun import Gun
from labs.day7.Target import Target

# print (dir(math))

BORDERS = [
    (0, 0), (800, 600)
]

Ball.BORDERS = BORDERS

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

t1 = Target(canvas)
g1 = Gun(canvas)

screen1 = canvas.create_text(400, 300, text='', font='28')

balls = []



def fireGun(event):
    ball = g1.fire2_end(event)
    if ball is not None:
        balls.append(ball)

def newGame(event=''):
    global g1, t1, screen1, balls
    print("New Game!")

    t1.new_target()

    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', fireGun)
    canvas.bind('<Motion>', g1.targeting)

    while t1.live or balls:
        for b in balls:
            b.move()
            b.draw(canvas)
            if t1.is_inside(b) and t1.live:
                t1.hit()
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bulletCount) + ' выстрелов')
        canvas.update()
        time.sleep(0.03)
        g1.targeting()
        g1.power_up()

        checkBalls(balls, canvas)

    print("End Game!")
    canvas.itemconfig(screen1, text='')
    # canvas.delete(gun)
    root.after(750, newGame())


newGame()

root.mainloop()