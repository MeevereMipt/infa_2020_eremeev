import numpy as np
import matplotlib.pyplot as pt

x = np.arange(-10, 10.01, 0.01)
pt.plot(x, (np.log(x*x + 1)-np.round(x)/10)/np.log(1+np.tan(1/(1+np.sin(x)**2))) )

pt.xlabel(r'$x$')
pt.ylabel(r'$f(x)$')
pt.title(r'$f(x)=$')
pt.grid(True)

pt.show()
