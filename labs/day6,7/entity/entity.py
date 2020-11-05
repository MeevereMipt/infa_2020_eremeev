import pygame as pg


class Entity():

    def __init__(self, score):
        # Arrays where entity belongs to
        self.arrays = []
        self.score = score

    def appendTo(self, array):
        array.append(self)
        self.arrays.append(array)

    def removeFrom(self, array):
        array.remove(self)
        self.arrays.remove(array)

    def removeFromAll(self):
        for array in self.arrays:
            array.remove(self)
        self.arrays = []

    def draw(self, screen : pg.Surface):
        """
            Draw entity on surface
        """
        pass

    def update(self, dt):
        """
            Update object for dt
        """
        pass

    def on_click(self, event):
        """
            Action that occurs on click
        """
        pass

    def isInside(self, point)->bool:
        """
            Tests if point is inside entity
        """
        pass

