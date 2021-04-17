import matplotlib.pyplot as plt
import numpy as np


# Das Quadrat von x schreibt man als x**2
def f2(x, N):
   g=(4/np.pi)*np.array([np.cos((2*i+1)*x)/((2*i+1)**2) for i in range(0,N+1)])
   return g.sum()

t1 = np.arange(-np.pi, np.pi, 0.005)

y0=np.array([np.pi/2 for t in t1])
y1=np.array([np.pi/2-f2(t,0) for t in t1])
y2=np.array([np.pi/2-f2(t,2) for t in t1])
y10=np.array([np.pi/2-f2(t,3) for t in t1])
y21=np.array([np.pi/2-f2(t,5) for t in t1])


plt.plot(t1, abs(t1), 'black', t1, y0, t1, y1, t1, y2, t1, y10, t1, y21)
plt.show()
