import pygame
import labs.day6.event as cevent


class CApp(cevent.CEvent):

    def __init__(self):
        cevent.CEvent.__init__(self)
        self.clock = pygame.time.Clock()
        self._running = True

        self.FPS = 30

    def on_init(self):
        return True

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        print("Goodbye")
        pygame.quit()

    def on_execute(self):
        # if not self.on_init():
        #     self._running = False
        self.on_init()

        while self._running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()
