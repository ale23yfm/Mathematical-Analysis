from pygments.lexers import math

def f(x):
    return x**2+4*x+5

def f_prime(x):
    return 2*x+4

#(a)
def gradient_desc(x0, eta, steps= 30):
    xs = [x0]
    x = x0
    for _ in range(steps):
        x = x - eta*f_prime(x)
        xs.append(x)
    return xs
#(b)

#(c)

#(d)

if __name__ == "__main__":
    f_min = (-4)/(2*1)
    print (f_min)
    x0 = 5
    v = gradient_desc(x0, 0.1)
    print("a. ", v)

    v = gradient_desc(x0, 0.2, 15)
    print("b. ", v)

    v = gradient_desc(x0, 0.7, 10)
    print("c. ", v)