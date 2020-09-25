import numpy as np
import turtle as t

def Vector(x,y):
    return np.array([[float(x),float(y)]])

def mag(vector):
    return np.sqrt(np.matmul(vector, np.transpose(vector))[0][0])

dt = 0.3
BORDERS = t.screensize()

E_X = Vector(1,0)
E_Y = Vector(0,1)

class Particle:


    def __init__(self):
        self.a = Vector(0,0)
        self.v = Vector(0,0)
        self.r = Vector(0,0)

        self.forces = [Force()]

        self.t = t.Turtle(shape="circle")
        self.t.speed(0)

    def update(self):

        if( self.r[0][0] <= -BORDERS[0] ):
            self.v[0][0] = abs(self.v[0][0])
        if (self.r[0][0] >= BORDERS[0]):
            self.v[0][0] = -abs(self.v[0][0])

        if (self.r[0][1] <= -BORDERS[1]):
            self.v[0][1] = abs(self.v[0][1])
        if (self.r[0][1] >= BORDERS[1]):
            self.v[0][1] = -abs(self.v[0][1])

        self.r += self.v * dt + self.a * dt * dt / 2
        self.v += self.a * dt

        self.a = sum(self.forces).force

        self.t.goto((self.r[0][0],self.r[0][1]))

class Force:


    def __init__(self):
        self.force = Vector(0,0)

    def __add__(self, other):
        f = Force()
        f.force = self.force + other.force
        return f

    def __mul__(self, other : int):
        f = self.__class__()

        def update(obj):

            self.force = other * self.force

        f.update = test


    def update(self):
        pass


class Gravitation(Force):


    def __init__(self, p1 : Particle, p2 : Particle):
        Force.__init__(self)
        self.G = 1
        self.p1 = p1
        self.p2 = p2


    def update(self):
        dr = self.p1.r - self.p2.r
        self.force = -self.G * (dr)/mag(dr)**3

p1,p2 = Particle(), Particle()
p1.r = Vector(100,0)
p2.r = Vector(-100,0)

f = Gravitation(p1,p2)
p1.forces.append(f)


t.exitonclick()