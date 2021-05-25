import matplotlib.pyplot as plt
import numpy as np

import scipy.integrate as integrate

# berechnet das Integral von (sin x)/x von 1 bis y 
# wenn [0] nicht am Ende steht wäre das Ergebnis ein Paar (Integralwert, Fehler)
def inte(y):
    return integrate.quad(lambda x: np.sin(x)/x , 0.001, y)[0]

# 'vektorisiert' die letzte Funktion
# jetzt darf hier für x auch ein array eingesetzt werden
def intevec(x):
    return np.array([inte(v) for v in x])
    
fig = plt.figure()
ax = fig.add_subplot(111)


x = np.arange(0.001, 50, 0.1)
y = np.arange(0.9, 50, 0.1)



ax.plot(x, np.sin(x)/x)
ax.plot(y, 1/y)

ax.plot(x, intevec(x))


plt.show()