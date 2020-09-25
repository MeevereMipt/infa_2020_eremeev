import pygame
from pygame.locals import *

class Eventer():

    def onQuit(self, event):
        self.finished = True
    
    def onMouseDown(self, event):
        pass

    def onMouseUp(self, event):
        pass

    def onKeyDown(self, event):
        pass

    def onKeyUp(self, event):
        pass


    def onEvent(self, event):
        if   event.type == QUIT:
            self.onQuit(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.onMouseDown(event)
        elif event.type == MOUSEBUTTONUP:
            self.onMouseUp(event)
        elif event.type == KEYDOWN:
            self.onKeyDown(event)
        elif event.type == KEYUP:
            self.onKeyUp(event)
