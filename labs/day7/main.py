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
Target.BORDERS = BORDERS

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)


g1 = Gun(canvas)

screen1 = canvas.create_text(400, 300, text='', font='28')

targets = [Target(canvas), Target(canvas)]
balls = []

def checkTargets():
    result = False
    for t in targets:
        result = result or t.live
    return result


def fireGun(event):
    ball = g1.fire2_end(event)
    if ball is not None:
        balls.append(ball)

def newGame(event=''):
    # global g1, t1, screen1, balls
    print("New Game!")

    for t in targets:
        t.new_target()

    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', fireGun)
    canvas.bind('<Motion>', g1.targeting)
    canvas.bind('<Button-3>', g1.cartridge.do_recharge)

    while balls or checkTargets():
        for b in balls:
            b.move()
            b.draw(canvas)

            for t in targets:
                if t.is_inside(b) and t.live:
                    t.hit()

        for t in targets:
            t.move()
            t.draw()

        if not checkTargets():
            canvas.bind('<Button-1>', '')
            canvas.bind('<ButtonRelease-1>', '')
            canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bulletCount) + ' выстрелов')

        canvas.update()
        time.sleep(0.03)
        g1.cartridge.recharge()
        g1.targeting()
        g1.power_up()

        checkBalls(balls, canvas)

    g1.bulletCount = 0
    canvas.itemconfig(screen1, text='')
    # canvas.delete(gun)
    root.after(750, newGame())


newGame()

root.mainloop()