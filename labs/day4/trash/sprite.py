import pygame as pg
import numpy as np

class Sprite():

    def __init__(self, s : pg.Surface, pos, area=None):
        self.surface = s
        self.pos = pos
        self.area = area

    def __str__(self):
        return self.surface.__str__()

def spriteRectangle(origin, position, color):
    #Костыль для получения numpy массивов
    c1 = np.add(origin, (0,0))
    c2 = np.add(position, (0,0))

    s = pg.Surface(tuple(abs(c2-c1)))
    s.fill(color)

    return Sprite(s, tuple(c1 + ((c2-c1)-abs(c2-c1))/2))