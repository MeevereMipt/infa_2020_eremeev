import pygame as pg
import numpy as np

import os


def drawSurface(s1, s2, pos, size=None):
    if size != None:
        s2transformed = pg.transform.scale(s2, size)
    else:
        s2transformed = s2

    s2size = np.add(s2transformed.get_size(), (0,0))
    pos    = np.add(pos, (0,0))

    s1.blit(s2transformed, tuple(pos - s2size/2))


def eskimoSurface():
    return pg.image.load(os.path.join("sprites", "eskimo.png"))

def iglooSurface():
    return pg.image.load(os.path.join("sprites", "igloo.png"))

def catSurface():
    return pg.image.load(os.path.join("sprites", "cat.png"))


WIDTH = 800
HEIGHT = 1000

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))



screen.fill(pg.Color("#E6E6E6"))

pg.draw.rect(screen, pg.Color("#F9F9F9"), (0, HEIGHT/2, WIDTH, HEIGHT))

drawSurface(screen, eskimoSurface(), (545, 599) )
drawSurface(screen, iglooSurface(), (229, 536) )
drawSurface(screen, catSurface(), (251, 764) )



finished = False
while not(finished):
    for event in pg.event.get():

        if event.type == pg.QUIT:
            finished = True

        # if event.type == pg.MOUSEBUTTONDOWN:
        #     print(event.pos)
        #     drawSurface(screen, catSurface(), event.pos )

    pg.display.update()

pg.quit()