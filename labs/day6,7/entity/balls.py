#Not mine
import numpy as np
import pygame as pg
from random import randint
import os

#My "bicycles"
from labs.day6.particles import Particle, vector, magnitude
from labs.day6.entity.entity import Entity

RED = "#FF0000"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
GREEN = "#00FF00"
MAGENTA = "#FF00FF"
CYAN = "#00FFFF"
BLACK = "#000000"
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pg.mixer.init()

class Ball(Particle, Entity):

    death_sounds = [
        pg.mixer.Sound(os.path.join("music","sounds","death1.ogg")),
        pg.mixer.Sound(os.path.join("music","sounds","death2.ogg")),
        pg.mixer.Sound(os.path.join("music","sounds","death3.ogg")),
        pg.mixer.Sound(os.path.join("music","sounds","death4.ogg")),
        pg.mixer.Sound(os.path.join("music","sounds","death5.ogg")),
    ]

    def __init__(self, r=vector(0, 0), radius=1, color=pg.Color("#FFFFFF"), v=vector(0, 0)):
        Particle.__init__(self, r, v)
        Entity.__init__(self, 1000 / radius)

        self.radius = radius
        self.color = color

    def draw(self, surface: pg.Surface):
        pg.draw.circle(surface, self.color, (int(self.r[0]), int(self.r[1])), self.radius)

    def isInside(self, point):
        if magnitude(point - self.r) <= self.radius:
            return True
        return False

    def on_click(self, event):
        self.death_sounds[randint(0,4)].play()
        self.removeFromAll()


# Функции для удобства
def newBall(screen: pg.Surface) -> Ball:
    return Ball(vector(randint(0, screen.get_width()), randint(0, screen.get_height())),
                randint(10, 50),
                pg.Color(COLORS[randint(0, 5)]),
                vector(randint(-20, 20), randint(-20, 20)))


def newBallAt(position) -> Ball:
    return Ball(vector(position[0], position[1]),
                randint(10, 100),
                pg.Color(COLORS[randint(0, 5)]),
                vector(randint(-10, 10), randint(-10, 10)))


if __name__ == "__main__":

    pg.init()
    screen = pg.display.set_mode((1200, 1000))

    balls = [newBall(screen) for i in range(10)]

    for ball in balls:
        ball.draw(screen)

    pg.display.update()

    finished = False
    while not finished:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                finished = True

    pg.quit()
