from random import randrange as rnd, choice
import tkinter as tk
import math

from labs.day7.CartridgeBall import CartridgeBall

class Gun():

    def __init__(self, canvas : tk.Canvas):
        self.f2_power = 10
        self.f2_on = False
        self.angle = 1
        self.id = canvas.create_line(20,450,50,420,width=7)

        self.canvas = canvas
        self.bulletCount = 0

        self.cartridge = CartridgeBall(canvas)

    def fire2_start(self, event):
        self.f2_on = True

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """

        new_ball = self.cartridge.takeAmmo()
        print(self.cartridge.ammo)
        if new_ball is not None:
            self.angle = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.angle)
            new_ball.vy = - self.f2_power * math.sin(self.angle)

        self.f2_on = False
        self.f2_power = 10

        self.bulletCount = self.cartridge.ammo

        return new_ball

    def targeting(self, event=None):
        """Прицеливание. Зависит от положения мыши."""
        if event is not None:
            self.angle = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
        self.canvas.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.angle),
                    450 + max(self.f2_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
