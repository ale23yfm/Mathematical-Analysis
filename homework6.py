import numpy as np

def function(n):
    return np.log(n+1)

def function_d(n):
    return 1/(n+1)

x = 0.5

exact = function_d(x)
hs = []
for k in range(1, 25):
    hs.append(10**(-k))

print(f"{'h':<15} | {'Forward Error':<25} | {'h^2':<15} | {'Central Error':<25}")

for h in hs:
    first = (function(x+h)-function(x))/h
    second = (function(x+h)-function(x-h))/(2*h)

    error_first = abs(first - exact)
    error_second = abs(second - exact)

    print(f"{h:<15.1e} | {error_first:<25.15e} | {h**2:<15.1e} | {error_second:<25.15e}")





