import numpy as np
import matplotlib.pyplot as plt


def wn(a, b, n, x):
    return b**n * np.cos(a**n * np.pi * x)


def W(a, b, x):
    n = 0
    r = 0.0
    eps = 1.0e-4
    while True:
        w_ = wn(a, b, n, x)
        r += w_
        if np.linalg.norm(w_) < eps:
            break
        n += 1
        print('n =', n, 'eps =', eps)
        return r


a = 3
b = 1/2
x = 1/2
n = 50

print("n =", n, "wn =", wn(a, b, n, x))
print(W(a, b, x))

xx = np.linspace(0.99999, 1.00001, 5000)
print('xx =', xx, type(xx))

plt.plot(xx, W(a, b, xx))
plt.show()

ww = sum(b**n*np.cos(a**n*np.pi*xx) for n in range(50))
plt.plot(xx, ww)
plt.show()

print(a**1000)



