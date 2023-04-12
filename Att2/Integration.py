import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, Integral, exp, log
from threading import Thread
from scipy.special import roots_legendre


def function(x):
    f = np.exp(x) * np.log(x)
    return f


def foo():
    _x = Symbol('x')
    return Integral(exp(_x) * log(_x), (_x, 1, 2))


def method_middle_rect(a, b, h):
    res = 0
    x = a
    while True:
        x += h
        res += function(x - h / 2)
        if x >= b:
            break

    res *= h
    print(str('Method of middle rectangles: ') + str(res))


def method_trapezoid(a, b, h):
    res = (function(a) + function(b)) / 2

    x = a + h
    while x < b:
        res += function(x)
        x += h

    res *= h
    print(str('Trapezoidal method: ') + str(res))


def method_Simpson(a, b, h):
    y_odd = 0.0
    y_even = 0.0

    x_s = []

    n = int(1 / h)

    for i in range(n + 1):
        x_s.append(a + i * h)

    for j in range(1, n, 2):
        y_odd += function(x_s[j])

    for k in range(2, n, 2):
        y_even += function(x_s[k])

    res = h / 3 * (function(a) + 4 * y_odd + 2 * y_even + function(b))
    print(str('Simpson\'s Method (Parabola Method): ') + str(res))


def method_Gaussian(a, b, n):
    b_a_half_size = (b - a) / 2
    a_b_half_sum = (a + b) / 2

    roots, weights = roots_legendre(n)

    _sum = 0
    for i in range(n):
        _sum += weights[i] * function(a_b_half_sum + b_a_half_size * roots[i])
    _sum *= b_a_half_size

    print(str('Gaussian quadrature: ') + str(_sum))


def draw_function():
    x = np.arange(0.1, 2.5, 0.07)
    f = function(x)

    line = plt.plot(x, f, color='limegreen')

    plt.fill_between(x, f, color='palegreen', where=(x < 2) & (f > 0))
    plt.grid()

    plt.setp(line, color="limegreen", linewidth=1.5)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.show()


def main():
    # _eps = 1 / 6
    _eps = 0.000001
    _a = 1
    _b = 2
    _n = 6

    print('\n' + str(foo()) + '\n')
    print('================================================================================================\n')

    thread1 = Thread(target=method_middle_rect, args=(_a, _b, _eps))
    thread2 = Thread(target=method_trapezoid, args=(_a, _b, _eps))
    thread3 = Thread(target=method_Simpson, args=(_a, _b, _eps))
    thread4 = Thread(target=method_Gaussian, args=(_a, _b, _n))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print('\n================================================================================================\n')

    draw_function()


if __name__ == '__main__':
    main()
