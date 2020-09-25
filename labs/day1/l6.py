import numpy as np
import matplotlib.pyplot as plt

def Weierstrass( x, a, b, n ):
    sum = 0
    for i in range(0, n):
        sum += (b**i) * np.cos((a**i) * np.pi * x)
    return sum

def Smth( x, n ):
    sum = 0
    for i in range(1, n):
        sum += np.sin( i*i * x)/i/i
    return sum


x = np.arange(-2, 2, 0.001)

plt.plot( x, Weierstrass(x, 3, 1/2, 35))

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x)=$')
plt.grid(True)

plt.show()


