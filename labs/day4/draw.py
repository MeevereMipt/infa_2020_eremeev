import pygame
import labs.day4.event as event


pygame.init()

class App(event.Eventer):


    def __init__(self):
        self.FPS = 30
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()


    def execute(self):
        self.finished = False
        while not self.finished:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                self.onEvent(event)
            self.onRender()
        self.onEnd()

    def onRender(self):
        pass

    def onEnd(self):


pygame.quit()