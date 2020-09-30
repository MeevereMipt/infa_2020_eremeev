import pygame as pg
import numpy as np

import os

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 1000
def drawSurface(s1, s2, pos, size=None, scale=None):
    s2transformed = s2
    s2size = np.add(s2.get_size(), (0, 0))

    if scale != None and size != None:
        raise AttributeError("At least attribute, either size or scale, must be none")

    if scale != None:

        if( scale[0] < 0 ):
            s2 = pg.transform.flip(s2, True, False)
        if( scale[1] < 0):
            s2 = pg.transform.flip(s2, False, True)

        s2transformed = pg.transform.scale(s2, (s2size[0]*abs(scale[0]), s2size[1]*abs(scale[1])))

    if size != None:

        if (size[0] < 0):
            s2 = pg.transform.flip(s2, True, False)
        if (size[1] < 0):
            s2 = pg.transform.flip(s2, False, True)

        s2transformed = pg.transform.scale(s2, (abs(size[0]), abs(size[1])))


    s2size = np.add(s2transformed.get_size(), (0,0))
    pos    = np.add(pos, (0,0))

    pos = (pos * [WIDTH, HEIGHT])// [DEFAULT_WIDTH, DEFAULT_HEIGHT]

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

# [287 605]
# (288, 140)
drawSurface(screen, iglooSurface(), (48, 500), (142, 102))
drawSurface(screen, iglooSurface(), (408, 483), (142, 102))
drawSurface(screen, iglooSurface(), (229, 536))
drawSurface(screen, iglooSurface(), (157, 605), (248, 180))
drawSurface(screen, iglooSurface(), (287, 665), (142, 102))

drawSurface(screen, eskimoSurface(), (687, 489), (76, 120))
drawSurface(screen, eskimoSurface(), (719, 600), (136, 144))
drawSurface(screen, eskimoSurface(), (624, 556), (56, 170))
drawSurface(screen, eskimoSurface(), (700, 657), (236, 92))
drawSurface(screen, eskimoSurface(), (462, 533), (116, 108))
drawSurface(screen, eskimoSurface(), (545, 599))
drawSurface(screen, eskimoSurface(), (473, 721), (156, 158))


drawSurface(screen, catSurface(), (251, 764))
drawSurface(screen, catSurface(), (774, 947))
drawSurface(screen, catSurface(), (662, 833))
drawSurface(screen, catSurface(), (13, 878))
drawSurface(screen, catSurface(), (313, 932))


finished = False
lastPoint = None

while not(finished):
    for event in pg.event.get():

        if event.type == pg.QUIT:
            finished = True

        # if event.type == pg.MOUSEBUTTONDOWN:
        #
        #     if lastPoint == None: #Means that we need to draw an image (no)
        #         lastPoint = event.pos
        #
        #     else: #Now we need to scale it
        #         pos = np.asarray(event.pos)
        #         lastPos = np.asarray(lastPoint)
        #
        #         print(pos)
        #         print(tuple(2*abs(lastPos-pos)))
        #
        #         drawSurface(screen, eskimoSurface(), pos, size=tuple(2*abs(lastPos-pos)) )
        #         lastPoint = None

        # if event.type == pg.MOUSEBUTTONDOWN:
        #     print(event.pos)
        #     drawSurface(screen, catSurface(), event.pos )

    pg.display.update()

pg.quit()