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

    """
        Draw entity on surface
    """
    def draw(self, screen : pg.Surface):
        pass

    """
        Update object for dt
    """
    def update(self, dt):
        pass

    """
        Action that occurs on click
    """
    def on_click(self, event):
        pass

    """
        Tests if point is inside entity
    """
    def isInside(self, point)->bool:
        pass

