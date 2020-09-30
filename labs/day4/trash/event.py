import pygame
from pygame.locals import *

class Eventer():

    def __init__(self):
        self.currentEvents = {}

    def onQuit(self, event):
        self.finished = True

    def onMouseMotion(self, event):
        pass

    def onMouseDown(self, event):
        self.currentEvents[MOUSEBUTTONDOWN] = event

    def onMouseUp(self, event):
        del self.currentEvents[MOUSEBUTTONDOWN]

    def onKeyDown(self, event):
        pass

    def onKeyUp(self, event):
        pass


    def onEvent(self, event):

        if event.type == MOUSEMOTION:
            self.onMouseMotion(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.onMouseDown(event)
        elif event.type == MOUSEBUTTONUP:
            self.onMouseUp(event)
        elif event.type == KEYDOWN:
            self.onKeyDown(event)
        elif event.type == KEYUP:
            self.onKeyUp(event)
        elif event.type == QUIT:
            self.onQuit(event)

