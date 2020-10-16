import numpy as np
import pygame as pg
from random import randint

from labs.day6.particles import Particle, vector, magnitude
from labs.day6.entity.entity import Entity

class Grub(Particle, Entity):

    def __init__(self, pos=vector(0,0), vel=vector(0,0)):
        Particle.__init__(self, pos, vel)
        pass

    def draw(self, screen : pg.Surface):
        pass

    def update(self):
        pass

    def on_click(self):
        pass
