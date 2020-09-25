import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]

p, V= np.polyfit(x, y, deg=3, cov=True)

plt.errorbar(x, y, xerr=0.05, yerr=0.1)

x_ = np.arange(x[0], x[x.__len__()-1], 0.01 )
plt.plot(x_, np.polyval(p, x_))

plt.grid()
plt.show()