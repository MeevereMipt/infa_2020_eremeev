import numpy as np
import pygame as pg

from random import randint

from labs.day5.particles import Particle, vector, magnitude


class Ball(Particle):

    def __init__(self, r=vector(0, 0), radius=1, color=pg.Color("#FFFFFF"), v=vector(0, 0)):
        Particle.__init__(self, r, v)

        self.radius = radius
        self.color = color

    def draw(self, surface: pg.Surface):
        pg.draw.circle(surface, self.color, self.r, self.radius)

    def isInside(self, point):
        if magnitude(point - self.r) <= self.radius:
            return True
        return False


RED = "#FF0000"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
GREEN = "#00FF00"
MAGENTA = "#FF00FF"
CYAN = "#00FFFF"
BLACK = "#000000"
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def newBall() -> Ball:
    return Ball(vector(randint(100, 1100), randint(100, 900)),
                randint(10, 100),
                pg.Color(COLORS[randint(0, 5)]))


if __name__ == "__main__":
    balls = [newBall() for i in range(10)]

    for ball in balls:
        ball.draw()

