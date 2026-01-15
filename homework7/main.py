import numpy as np
import matplotlib.pyplot as plt

def gradient_Descending(b, x0=2.0, y0=2.0, steps=15):
    x, y = x0, y0
    f = [(x, y)]
    for i in range(steps):
        gradient = np.array([x, b*y])
        epsilon = 1e-12
        sk = (x ** 2 + b ** 2 * y ** 2) / (x ** 2 + b ** 3 * y ** 2 + epsilon)
        x = x - sk * gradient[0]
        y = y - sk * gradient[1]
        f.append((x, y))
    return np.array(f)

b = [1, 1/2, 1/5, 1/10, 1/20, 1/40, 1/80]

X, Y = np.meshgrid(np.linspace(-2.5, 2.5, 400),np.linspace(-2.5, 2.5, 400))

for bb in b:
    Z = 0.5 * (X**2 + bb * Y**2)
    f = gradient_Descending(bb)
    plt.figure()
    plt.contour(X, Y, Z)
    plt.plot(f[:, 0], f[:, 1], marker='o')
    plt.title(f"Gradient Descent for b = {bb}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(f"gradient_descent_b_{bb}.png")  # save instead of show
    plt.close()



