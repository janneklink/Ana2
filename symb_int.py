import sympy as sp
# https://docs.sympy.org/latest/modules/integrals/integrals.html

sp.init_printing(use_unicode=False, wrap_line=False)
x = sp.Symbol('x')
p = sp.Symbol('p')

a=sp.integrate(x**2 + x + 1, x)
b=sp.integrate(1/(x**2 + x + 1), x)
c=sp.integrate(x**2 * sp.cos(p*x), x)
d=sp.integrate(x**2 * sp.cos(x)*sp.exp(x), x)

e=sp.integrate(sp.exp(x**2),x) 
# e ist nicht explizit ausführbar. Weil es aber öfter vorkommt, hat das  
# einen Namen.

f=sp.integrate(sp.exp(x**3),x) 
# wie auch e ist f nicht explizit, aber es wird auf Standard-spezielle-Funktionen
# zurückgeführt
# \Gamma-Funktion: 6.1.1 https://secure.math.ubc.ca/~cbm/aands/page_255.htm
# \gamma-Funktion: 6.5.2 https://secure.math.ubc.ca/~cbm/aands/page_260.htm


# atan =arctan
g=sp.integrate(sp.exp(x**4)*sp.atan(x),x) 

h=sp.integrate(p*x**2 + x + 1, x)

