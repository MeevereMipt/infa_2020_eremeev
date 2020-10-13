import numpy as np


def vector(x, y):
    return np.array([float(x), float(y)])


def magnitude(v):
    return np.sqrt(np.dot(v, v))


dt = 0.3
BORDERS = ((0, 0), (800, 800))

E_X = vector(1, 0)
E_Y = vector(0, 1)


class Particle:

    def __init__(self, r=vector(0, 0), v=vector(0, 0)):
        self.a = vector(0, 0)
        self.v = v
        self.r = r

        self.forces = [Force()]

    def update(self):
        if self.r[0] <= -BORDERS[0][0]:
            self.v[0] = abs(self.v[0])
        if self.r[0] >= BORDERS[1][0]:
            self.v[0] = -abs(self.v[0])

        if self.r[1] <= -BORDERS[0][1]:
            self.v[1] = abs(self.v[1])
        if self.r[1] >= BORDERS[1][1]:
            self.v[1] = -abs(self.v[1])

        self.r += self.v * dt + self.a * dt * dt / 2
        self.v += self.a * dt

        self.a = sum(self.forces, Force()).force


class Force:

    def __init__(self):
        self.force = vector(0, 0)

    def __add__(self, other):
        class Test(Force):
            def update(self):
                self.force = self.force + other.force

        return Test()

    def __mul__(self, other: int):
        class Test(Force):
            def update(self):
                self.force = other * self.force

        return Test()

    def update(self):
        pass
