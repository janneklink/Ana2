import matplotlib.pyplot as plt
import numpy as np


def f2(x, N):
    g = 4 / np.pi * np.array([np.sin((2 * i + 1) * x) / (2 * i + 1) for i in range(0, N + 1)])
    return g.sum()


t1 = np.arange(-np.pi, np.pi, 0.01)
t2 = np.arange(-np.pi, 0, 0.01)
t3 = np.arange(0, np.pi, 0.01)

x0 = np.array([-1 for t in t2])
x1 = np.array([1 for t in t3])

y0 = np.array([f2(t, 0) for t in t1])
y1 = np.array([f2(t, 1) for t in t1])
y2 = np.array([f2(t, 5) for t in t1])
y10 = np.array([f2(t, 10) for t in t1])
y21 = np.array([f2(t, 21) for t in t1])

plt.plot(t2, x0, 'black', t3, x1, 'black', t1, y0, t1, y1,
         t1, y2, t1, y10, t1, y21)
plt.show()
