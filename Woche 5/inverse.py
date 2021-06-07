# scipy: https://www.scipy.org/scipylib/index.html
from scipy import optimize

import matplotlib.pyplot as plt
import numpy as np

# lambda-Kalkül -- eine Möglichkeit in Python Funktionen zu
# spezifizieren
f = lambda x, a: x ** 3 - a
fder = lambda x, a: 3 * x ** 2

x = np.arange(-50, 50, 1)
# x = [1]*100
a = np.arange(-50, 50, 1)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html#scipy.optimize.newton
vec_res = optimize.newton(f, x, fprime=fder, args=(a,))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a, np.sign(a) * np.abs(a) ** (1 / 3))
ax.plot(a, vec_res, '.')

plt.show()
