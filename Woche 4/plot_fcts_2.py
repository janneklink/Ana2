import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

def fun(x, y):
    return x*y/(x**2+y**2)
    #return x**2-y**2
    


fig = plt.figure()
ax = plt.axes(projection='3d')


x  = y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(x, y)
Z = np.array(fun(X, Y))

# Was macht rcount/ccount und was passiert, wenn das nicht da steht?
# Siehe https://matplotlib.org/ (Suchen nach plot_surface)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, 
                       rcount=200, ccount=200)


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
