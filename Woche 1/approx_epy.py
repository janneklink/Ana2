# Python-Programm -- plot von Approximationen von e, 
# einmal mittels der Taylorpolynome und einmal mittels der Folge vom 
# Zinseszins

# import = importiert Programmbibliotheken
# matplotlib: https://de.wikipedia.org/wiki/Matplotlib
# numpy: https://de.wikipedia.org/wiki/NumPy
#
# Funktionen aus den Bibliotheken werden dann mittels 
# Name-der-Biblio.Funktionsname aufgerufen. Da der Bibliotheksname
# oft lang ist, kann man ABkürzungen einführen:
#    import Name-der-Biblio as kurzer-Name 
import matplotlib.pyplot as plt
import numpy as np

# Definition einer Funktion, die das n-te Taylorpolynom von e^x bei x=1 
# ausgibt:
# prod ist eine Funktion aus numpy - deshalb hier mit np.prod
# prod nimmt einen array und multipliziert die Einträge
# hier kommt der array aus range(1,n+1) und enthält alle nat.Zahlen ab 1, die
# kleiner als n+1 sind.

def etaylor(n): 
	return sum(1/np.prod(range(1,d+1)) for d in range(0, n+1))


# Bereich der Werte für die nachher die Funktionen gezeichnet werden
t = range(1, 40)

# erzeugt den Plot mit t auf der x-Achse und einmal (1+1/t)^t auf der
# y-Achse für alle t in dem eben definierten array
# 'bs' steht für 'blue squares'
# 'rs' steht für 'red squares', damit wird etaylor(s) dargestellt
plt.plot(t, [np.power(1+1/s,s) for s in t], 'bs',  
            [etaylor(s) for s in t], 'rs')

# zeigt den Plot  an
plt.show()
