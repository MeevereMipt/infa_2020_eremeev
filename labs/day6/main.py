import labs.day6.app.app as capp
import labs.day6.entity.balls as balls

from labs.day6.entity.balls import BLACK

import pygame as pg

WIDTH = 800
HEIGHT = 800


class App(capp.CApp):

    def __init__(self):
        capp.CApp.__init__(self)

        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.entities = []
        self.score = 0

    def on_init(self):
        capp.CApp.on_init(self)
        [balls.newBall(self.screen).appendTo(self.entities) for i in range(100)]

    def on_mbutton_down(self, event):
        """
        Method of handling mouse-down event
        :param event:
        :return:
        """
        for entity in self.entities:
            if entity.isInside(event.pos):
                self.score += int(entity.score)
                entity.on_click(event)
                return

        self.score -= 50

    def on_render(self):
        self.screen.fill(pg.Color(BLACK))

        #рисуем шарики
        for entity in self.entities:
            entity.draw(self.screen)

        #рисуем счётчик очков
        font = pg.font.SysFont('comicsansms', 36)
        text = font.render("Scores : "+str(self.score), 1, pg.Color("#FFFFFF"))
        self.screen.blit(text, (10, 10))

        pg.display.update()

    def on_loop(self):
        for ball in self.entities:
            ball.update()


if __name__ == "__main__":
    app = App()
    app.on_execute()
