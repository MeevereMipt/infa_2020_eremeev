#Not mine
import numpy as np
import pygame as pg
from random import randint

#My "bicycles"
from labs.day6.particles import Particle, vector, magnitude
from labs.day6.entity.entity import Entity
from labs.day6.entity.balls import Ball

RED = "#FF0000"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
GREEN = "#00FF00"
MAGENTA = "#FF00FF"
CYAN = "#00FFFF"
BLACK = "#000000"
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class BadBall( Ball ):

    def __init__(self, r=vector(0, 0), radius=1, color=pg.Color("#FFFFFF"), v=vector(0, 0)):
        Ball.__init__(self, r, radius, color, v)
        self.score = int(-1000/radius)

