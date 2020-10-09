import pygame
import labs.day5.event as cevent


class CApp(cevent.CEvent):

    def __init__(self):
        cevent.CEvent.__init__(self)
        self._running = True

    def on_init(self):
        pygame.init()
        self._running = True    #inner variable, currently manages the loop

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        print("Goodbye")
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()
