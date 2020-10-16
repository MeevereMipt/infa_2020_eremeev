import numpy as np

class clickRegion():

    def __init__(self, zindex):
        self.zindex = zindex

    def isInside(self, point)->bool:
        pass



class clickBox():

    def __init__(self, v1, v2, zindex):
        self.zindex = zindex
        self.v1 = v1
        self.v2 = v2

    def isInside(self, point):
        pass
