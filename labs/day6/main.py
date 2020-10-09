import labs.day6.app as capp
import labs.day6.balls as balls

from labs.day6.balls import COLORS, BLACK, RED, GREEN, BLUE

import pygame as pg

WIDTH = 800
HEIGHT = 800


class App(capp.CApp):

    def __init__(self):
        capp.CApp.__init__(self)

        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.balls = []
        self.score = 0

    def on_init(self):
        capp.CApp.on_init(self)
        self.balls = [balls.newBall(self.screen) for i in range(50)]

        print(self.balls)

    def on_mbutton_down(self, event):
        ball_to_delete = None
        for ball in self.balls:
            if ball.isInside(event.pos):
                ball_to_delete = ball
                break

        if ball_to_delete is None:
            self.score -= 50
            return
        self.score += int(1000/ball_to_delete.radius)
        self.balls.remove(ball_to_delete)

    def on_render(self):
        self.screen.fill(pg.Color(BLACK))

        #рисуем шарики
        for ball in self.balls:
            ball.draw(self.screen)

        #рисуем счётчик очков
        font = pg.font.SysFont('comicsansms', 36)
        text = font.render("Scores : "+str(self.score), 1, pg.Color("#FFFFFF"))
        self.screen.blit(text, (10, 10))

        pg.display.update()

    def on_loop(self):
        for ball in self.balls:
            ball.update()


if __name__ == "__main__":
    app = App()
    app.on_execute()
