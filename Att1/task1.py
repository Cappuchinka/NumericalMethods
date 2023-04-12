import matplotlib.pyplot as plt
import numpy as np


def foo(x):
    return x * x * np.sin(x) + np.cos(x * x)


def diff_foo(x, step):
    return (foo(x + step) - foo(x - step)) / (2 * step)


def bisection_method(a, b, eps):
    ksi = (a + b) / 2.0
    if (np.abs(foo(a) - foo(b)) <= eps) or (np.abs(foo(ksi)) <= eps):
        return (a + b) / 2.0
    if foo(a) * foo(ksi) <= 0.0:
        return bisection_method(a, ksi, eps)
    else:
        return bisection_method(ksi, b, eps)


def chord_method(a, b, eps):
    x_i = a - ((foo(a) * (b - a)) / (foo(b) - foo(a)))
    while np.abs(x_i - a) > eps:
        a = x_i
        x_i = a - ((foo(a) * (b - a)) / (foo(b) - foo(a)))
    return x_i


def newton_method(b, eps):
    x_i = b - foo(b) / diff_foo(b, 0.25)
    while np.abs(x_i - b) > eps:
        b = x_i
        x_i = b - foo(b) / diff_foo(b, 0.25)
    return x_i


def draw_function():
    x = np.arange(_eps ** 2, 5.0, 0.01)
    f = foo(x)
    line = plt.plot(x, f, color='r')
    plt.grid()

    plt.setp(line, color="red", linewidth=1.5)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.show()


_eps = 0.00001  # epsilon
_a = 0.1
_b = 100

print('f(x) = 2x² - x - np.sin(x) - 1\n')
print('Bisection Method: ' + str(bisection_method(_a, _b, _eps)))
print('Chord Method: ' + str(chord_method(_a, _b, _eps)))
print('Newton Method: ' + str(newton_method(_b, _eps)))
draw_function()
