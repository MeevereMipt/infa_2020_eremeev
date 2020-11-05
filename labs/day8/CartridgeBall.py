from labs.day8.Cartridge import Cartridge
from labs.day8.Ball import Ball

class CartridgeBall(Cartridge):

    ammoType = Ball

    def takeAmmo(self):
        ball = Cartridge.takeAmmo(self)
        if ball is not None:
            ball.r += 5
        return ball
