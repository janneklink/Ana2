from math import cos, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def fun(x, y):
    z = [[0.0 for j in range(len(x[i]))] for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[i])):
            z[i][j] = f(x[i][j], y[i][j])
    return z


def f(x, y):
    return x*x-y*y


fig = plt.figure()
ax = plt.axes(projection='3d')

x = y = np.arange(-2, 2, 0.01)
X, Y = np.meshgrid(x, y)
Z = np.array(fun(X, Y))

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
