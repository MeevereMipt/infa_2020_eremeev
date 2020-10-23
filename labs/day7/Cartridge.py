import tkinter as tk
import math

class Cartridge:

    size = 3
    fullRechargeTime = 100
    ammoType = object

    bodySize = (30,10)

    def __init__(self, canvas : tk.Canvas):
        self.recharging = False
        self.rechargeTime = 0

        self.ammo = self.size

        self.centerPoint = (50,470)
        self.body = canvas.create_rectangle(
            self.centerPoint[0] - self.bodySize[0],
            self.centerPoint[1] - self.bodySize[1],
            self.centerPoint[0] + self.bodySize[0],
            self.centerPoint[1] + self.bodySize[1],
            fill="#000"
        )
        self.ammoRect = []
        self.ammoRectSize = (
            self.bodySize[0]/self.ammo,
            self.bodySize[1]/3*2
        )
        for i in range(self.ammo):
            point = (self.centerPoint[0] - self.bodySize[0] + (2 * i + 1) * self.ammoRectSize[0], self.centerPoint[1])
            self.ammoRect.append(canvas.create_rectangle(
                point[0] - self.ammoRectSize[0],
                point[1] - self.ammoRectSize[1],
                point[0] + self.ammoRectSize[0],
                point[1] + self.ammoRectSize[1],
                fill="#0f0"
            ))

    def takeAmmo(self):
        if not(self.recharging) and self.ammo <= 0:
            return None
        self.ammo -= 1
        return self.ammoType()

    def do_recharge(self):
        self.recharging = True
        self.rechargeTime = self.fullRechargeTime/self.size*self.ammo

    def recharge(self):
        if self.rechargeTime < self.fullRechargeTime:
            self.rechargeTime += 1
            self.ammo = round(self.rechargeTime/self.fullRechargeTime*self.size)
        else:
            self.recharging = False
