import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, simplify, N

x_coords = np.array([-4, -1, 1, 2, 4], dtype=float)
y_coords = np.array([3, 8, 1, -2, 4], dtype=float)


def lagrange(x, y, t):
    z = 0
    for i in range(len(y)):
        _y = y[i]
        for j in range(len(x)):
            if i != j:
                _y *= ((t - x[j]) / (x[i] - x[j]))
        z += _y

    return z


_t = Symbol('t')
print(N(simplify(lagrange(x_coords, y_coords, _t)), 4))

x_new = np.linspace(np.min(x_coords), np.max(x_coords), 100)
y_new = [lagrange(x_coords, y_coords, i) for i in x_new]
plt.plot(x_coords, y_coords, 'o', x_new, y_new)
plt.grid(True)
plt.show()
