import labs.day6.app.app as capp
import labs.day6.entity.balls as balls
import labs.day6.entity.grub as grub
import labs.day6.entity.badball as badball

from labs.day6.entity.balls import BLACK

import pygame as pg
import os

WIDTH = 900
HEIGHT = 700

N = 10

STATE_GAME = 0
STATE_END  = 1

class App(capp.CApp):

    def __init__(self):
        capp.CApp.__init__(self)

        pg.init()

        self.lastClickTime = 0
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.entities = []
        self.score = 0

        self.state = STATE_GAME

    def on_init(self):
        capp.CApp.on_init(self)

        pg.mixer.music.load(os.path.join("music","music","temp_DWtD2.ogg"))
        pg.mixer.music.play(10)

        [balls.newBall(self.screen).appendTo(self.entities) for i in range(N)]
        [grub.newGrub(self.screen).appendTo(self.entities) for i in range(N)]

    def on_mbutton_down(self, event):
        """
        Method of handling mouse-down event
        :param event:
        :return:
        """
        self.lastClickTime = pg.time.get_ticks()

        for entity in self.entities:
            if entity.isInside(event.pos):
                self.score += int(entity.score)
                entity.on_click(event)
                return

        self.score -= 50

    def on_render(self):
        self.screen.fill(pg.Color(BLACK))
        if self.state == STATE_GAME:
            #рисуем шарики
            for entity in self.entities:
                entity.draw(self.screen)

            #рисуем счётчик очков
            font = pg.font.SysFont('comicsansms', 36)
            text = font.render("Score : "+str(self.score), 1, pg.Color("#FFFFFF"))
            self.screen.blit(text, (10, 10))
        elif self.state == STATE_END:

            font = pg.font.SysFont('comicsansms', 72)
            text = font.render("Congratulations!", 1, pg.Color("#FFFFFF"))

            self.screen.blit(text, ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 2 - 36))

            font = pg.font.SysFont('comicsansms', 72)
            text = font.render("Your score is :" + str(self.score), 1, pg.Color("#FFFFFF"))

            self.screen.blit(text, ((self.screen.get_width() - text.get_width())//2 , self.screen.get_height()//2 + 36))
        pg.display.update()

    def on_loop(self):
        if self.state == STATE_GAME:
            for entity in self.entities:
                entity.update()

            if (pg.time.get_ticks()-self.lastClickTime) % 5000 > 2500:
                for entity in self.entities:
                    if entity.__class__ != badball.BadBall:
                        return
                self.state = STATE_END
                pg.mixer.Sound(os.path.join("music","sounds","cheer2.ogg")).play()
        elif self.state == STATE_END:
            pass



if __name__ == "__main__":
    app = App()
    app.on_execute()
