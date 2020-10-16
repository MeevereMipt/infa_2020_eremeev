import numpy as np
import pygame as pg
from random import randint, random

from labs.day6.particles import Particle, vector, magnitude
from labs.day6.entity.entity import Entity

from labs.day6.entity.balls import Ball, COLORS
from labs.day6.entity.badball import BadBall


class Grub(Particle, Entity):

    def __init__(self, pos=vector(0,0), radius=1, color=pg.Color("#FFFFFF"), vel=vector(0,0)):
        Particle.__init__(self, pos, vel)
        Entity.__init__(self, 1000 / radius)

        nearbyBalls = []
        for i in range(randint(2,5)):
            randomAngle = 2*np.pi*random()
            nearbyBalls.append((radius * np.asarray((np.cos(randomAngle), np.sin(randomAngle))),
                                randint(10,20)))
        self.balls = nearbyBalls

        self.radius = radius
        self.color = color

    def draw(self, screen : pg.Surface):
        for ball in self.balls:
            pos = self.r+ball[0]
            pg.draw.circle(screen, pg.Color("#FFFFFF"), (int(pos[0]),int(pos[1])), ball[1])
        pg.draw.circle(screen, self.color, np.vectorize(int)(self.r), self.radius)


    def isInside(self, point):
        if magnitude(point - self.r) <= self.radius:
            return True
        return False

    def on_click(self, event):
        balls = []
        for ball in self.balls:
            balls.append(BadBall(self.r + ball[0], ball[1],v=self.v+vector(randint(-5,5),randint(-5,5))))

        print(self.arrays)
        for array in self.arrays:
            for ball in balls:
                ball.appendTo(array)
        self.removeFromAll()



def newGrub(screen: pg.Surface) -> Grub:
    return Grub(vector(randint(0, screen.get_width()), randint(0, screen.get_height())),
                randint(10, 50),
                pg.Color(COLORS[randint(0, 5)]),
                vector(randint(-20, 20), randint(-20, 20)))