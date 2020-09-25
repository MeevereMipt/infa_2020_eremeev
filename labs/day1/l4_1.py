from numpy import *
import matplotlib.pyplot as pt

func = input()

x = arange(-10, 10.01, 0.01)
eval('pt.plot(x,'+func+')')

pt.xlabel(r'$x$')
pt.ylabel(r'$f(x)$')
pt.title(r'$'+func+'$')
pt.grid(True)

pt.show()