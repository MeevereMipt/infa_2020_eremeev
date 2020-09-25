import numpy as np

x = float(input())

y = (1/(np.sin(x) + 1) - np.log( 5/4 + 1/x**15 ))/np.log(1+x*x)

print(y)