import numpy as np
import matplotlib.pyplot as plt
# odeint - Für GDGL erster Ordnung
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
from scipy.integrate import odeint

# y'=a*y+b
def exp(y, x, a,b):
    return a*y+b

# y'=a*y*(b-y)
def autokat(y, x, a,b):
    return a*y*(b-y)

# y''+a*y=0 
# hier als: y'=z, z'=-a*y  (y[0]=y, y[1]=z)
def schwing(y, x, a):
    return [y[1], -a*y[0]]

x = np.linspace(0, 1, 30)

# 2x2 - Plots : 221 ist der oben links
plt.subplot(221)

#plottet die Lösung von exp für (a,b)=(2,0) und jeweils die Anfangswerte -1,0,1
# bei 0 (immer der erste Eintrag im Vektor x)
plt.plot(x, odeint(exp,[-1,0,1],x, args=(2, 0)))

#222 - Plot oben rechts
plt.subplot(222)
plt.plot(x, odeint(exp,[-1,0,1],x, args=(2, 2,)))

#223 - Plot unten links
plt.subplot(223)
plt.plot(x, odeint(autokat,[1,2, 4, 5,6 ],x, args=(1,4)))

#224 - Plot unten rechts
# da schwing eine DGl für y und z=y' ist, gibt odeint auch (y(t), z(t)) zurück
# wollen wir nur y(t) plotten müssen wir hinten [:,0] ransetzen
plt.subplot(224)
plt.plot(x, odeint(schwing,[1,0],x, args=(15,))[:,0])
plt.plot(x, odeint(schwing,[1,3],x, args=(15,))[:,0])

plt.show()

