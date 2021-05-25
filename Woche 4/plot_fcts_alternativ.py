from math import sqrt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def fun(x, y):
    return x ** 2 + x * y + y ** 2 - (
            x ** 3 + y * x ** 2 + x * y ** 2 + y ** 3) / (16 * sqrt(2))


# Definition der Reskalierungsfunktion 
# (kann man sich mit plt.plot(x,rescal(x)) anzeigen lassen)
def rescal(x):
    return x * np.sqrt((.03 + x ** 2) / 1.03)


fig = plt.figure()
ax = plt.axes(projection='3d')

# x = y = rescal(np.arange(-1, 1, 0.01))
# X, Y = np.meshgrid(x, y)


## Alternative Gitter mit Polarkoordinaten
r = np.arange(0, 2, 0.01)
p = np.arange(0, 2 * np.pi, 0.01)
R, P = np.meshgrid(r, p)
X, Y = R * np.cos(P), R * np.sin(P)

Z = np.array(fun(X, Y))

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
