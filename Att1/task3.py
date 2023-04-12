import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, simplify, N

x_coords = np.array([1, 3, 5, 7, 9], dtype=float)
y_coords = np.array([-1, 2, 3, -2, -6], dtype=float)


def _finite_difference(k, Y, i):
    if k == 0:
        return Y[i]
    elif k == 1:
        return Y[i + 1] - Y[i]
    else:
        return _finite_difference(k - 1, Y, i + 1) - _finite_difference(k - 1, Y, i)


def finite_difference(k, Y):
    return _finite_difference(k, Y, 0)


def a_n(k, prev, Y, h):
    if k == 0:
        return Y[0]
    else:
        return prev / (finite_difference(k - 1, Y) * k * h) * finite_difference(k, Y)


def newton(X, Y, T):
    _h = np.abs(X[1] - X[0])
    result = 0
    result += Y[0]
    a = Y[0]

    for i in range(1, len(Y)):
        a = a_n(i, a, Y, _h)
        t = a
        for j in range(i):
            t *= (T - X[j])
        result += t

    return result


_t = Symbol('t')
print(N(simplify(newton(x_coords, y_coords, _t)), 4))

x_new = np.linspace(np.min(x_coords), np.max(x_coords), 100)
y_new = [newton(x_coords, y_coords, i) for i in x_new]
plt.plot(x_coords, y_coords, 'o', x_new, y_new)
plt.grid(True)
plt.show()
