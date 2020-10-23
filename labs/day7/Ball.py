from random import randrange as rnd, choice
import tkinter as tk

class Ball:

    BORDERS = [(0,0),(0,0)]
    K = 0.02
    Vmin = 5

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])

        self.id = None

    def draw(self, canvas : tk.Canvas):
        if self.id is None:
            self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy

        self.vy -= 2 + self.vy*self.K
        self.vx -= self.vx*self.K

        if self.x < self.BORDERS[0][0]:
            self.vx = abs(self.vx)
        if self.x > self.BORDERS[1][0]:
            self.vx = -abs(self.vx)
        if self.y < self.BORDERS[0][1]:
            self.vy = -abs(self.vy)
        if self.y > self.BORDERS[1][1]:
            self.vy = abs(self.vy)

    @property
    def live(self):
        magnitudeSquared = self.vx**2 + self.vy**2
        return magnitudeSquared - self.Vmin**2

def checkBalls(balls, canvas : tk.Canvas):
    deadBalls = []
    for ball in balls:
        if ball.live < 0:
            canvas.delete(ball.id)
            deadBalls.append(ball)
    for ball in deadBalls:
        balls.remove(ball)
