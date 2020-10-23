from random import randrange as rnd, choice
import tkinter as tk
import math

from labs.day7.Ball import Ball

class Target():

    def __init__(self, canvas : tk.Canvas):
        self.points = 0
        self.live = True
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,0,0)
        self.id_points = canvas.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        self.canvas.coords(self.id, x-r, y-r, x+r, y+r)
        self.canvas.itemconfig(self.id, fill=color)

        self.live = True

    def is_inside(self, ball : Ball):
        """Функция проверяет сталкивалкивается ли шарик с целью, описываемый в обьекте obj.

                Args:
                    obj: Обьект, с которым проверяется столкновение.
                Returns:
                    Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        d = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
        if d < self.r + ball.r:
            return True
        return False

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        self.canvas.itemconfig(self.id_points, text=self.points)

        self.live = False