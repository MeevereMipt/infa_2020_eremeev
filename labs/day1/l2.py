import numpy as np
import matplotlib.pyplot as pt

x = np.arange(-10, 10.01, 0.01)
pt.plot(x, x*x - x - 6)

pt.xlabel(r'$x$')
pt.ylabel(r'$f(x)$')
pt.title(r'$f(x)=x^{2} - x - 6$')
pt.grid(True)

pt.show()