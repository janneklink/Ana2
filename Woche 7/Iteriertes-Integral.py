from scipy import integrate


# Definition von f als Funktion in zwei Variablen
f = lambda y, x: x*y

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html#scipy.integrate.dblquad
# Integrale von f
# auf der Menge 0\leq x \leq 2, 0\leq y \leq 1
I1=integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: 1)

print(I1)

# die Integrationsgrenzen des Integrals über y kann 
# i.A von x abhängen und werden deshalb selbst als 
# Funktion spezifiziert

# Integral auf der Menge 0\leq x \leq 2, 0\leq y \leq x^2
I2=integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: x**2)

print(I2)