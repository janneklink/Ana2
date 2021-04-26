# Fibonacci-Folge 

# zählt Anzahl der Fibonaccizahlen, die kleiner als n sind und 
# gibt außerdem diese Fibonaccizahlen aus

def fibonacci(n):
    a = 0
    b = 1
    i = 0
    while b < n:
        print(b)
        # die nächste Zeile ordnet dem 'neuen' a das 'alte' b zu
        # und dem 'neuen' b das 'alte' a+b 
        a, b = b, a+b
        # nächste Zeile: das 'neue' i ist das 'alte' i+1
        i += 1
    print('Anzahl der Fibonaccizahlen <', n, ':', i)
        
    
    
fibonacci(100.5)   