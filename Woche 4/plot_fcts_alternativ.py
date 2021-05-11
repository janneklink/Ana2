import numpy as np
import matplotlib.pyplot as plt


def fun(x, y):
    return x*y/(x**2+y**2)


# Definition der Reskalierungsfunktion 
# (kann man sich mit plt.plot(x,rescal(x)) anzeigen lassen)
def rescal(x):
   return x*np.sqrt((.03+x**2)/1.03)



fig = plt.figure()
ax = plt.axes(projection='3d')




x = y = rescal(np.arange(-1, 1, 0.01))
X, Y = np.meshgrid(x, y)


## Alternative Gitter mit Polarkoordinaten
#r = np.arange(0,1, 0.01)
#p = np.arange(0, 2*np.pi, 0.01)
#R,P = np.meshgrid(r,p)
# X,Y = R*np.cos(P), R*np.sin(P)




Z = np.array(fun(X, Y))


ax.plot_surface(X, Y, Z)






plt.show()



