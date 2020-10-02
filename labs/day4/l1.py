import pygame as pg
import numpy as np

import os


DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 600
def drawSurface(s1, s2, pos, size=None):
    if size != None:
        s2transformed = pg.transform.scale(s2, size)
    else:
        s2transformed = s2

    s2size = np.add(s2transformed.get_size(), (0,0))
    pos    = np.add(pos, (0,0))

    s1.blit(s2transformed, tuple(pos - s2size//2))


def smileSurface():
    return pg.image.load(os.path.join("sprites", "smile.png"))


WIDTH = 400
HEIGHT = 400

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))



screen.fill(pg.Color("#E6E6E6"))
drawSurface(screen, smileSurface(), (200, 200))



finished = False
lastPoint = None

while not(finished):
    for event in pg.event.get():

        if event.type == pg.QUIT:
            finished = True

    pg.display.update()

pg.quit()