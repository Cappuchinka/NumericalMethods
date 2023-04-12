import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from threading import Thread

EULER = None
SMART_EULER = None
ROOTS_RUNGE_KUTTA = None
ADAMS = None

K_1_4 = None

def getResult(matrix, y_id):
    result_table = PrettyTable()
    result_table.field_names = ["X", "Y"]
    for i in range(len(matrix[0])):
        result_table.add_row([matrix[0][i], matrix[y_id][i]])
    print(result_table.get_string())


def draw_function(Euler, SmartEuler, Runge_Kutta, Adams):

    plt.plot(Euler[0], Euler[1], color='red', label='Euler')
    plt.plot(SmartEuler[0], SmartEuler[1], color='blue', label='Smart Euler')
    plt.plot(Runge_Kutta[0], Runge_Kutta[1], color='green', label='Runge-Kutta')
    plt.plot(Adams[0], Adams[1], color='magenta', label='Adams')

    plt.grid()
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.legend()

    plt.show()


def function(x, y):  # x ∈ [0; 1], y(0) = 2, h = 0.1
    return (4 * x + 2 * y) / (2 * x + 1)


# def function(x, y): # x ∈ [0; 2], y(0) = 1, h = 0.5
#     return x - y

# def foo(x, y):
#    return

# def function(x, y):
#    return 8 / x * foo(x, y) - 3*y

def Euler(y_0, h, a, b):
    _roots = [[0] * 1 for _ in range(2)]
    _roots[0][0] = a
    _roots[1][0] = y_0
    n = np.abs(a - b) / h + 1

    i = 1
    while i < n + 1:
        _roots[0].append(_roots[0][i - 1] + h)
        _roots[1].append(_roots[1][i - 1] + h * function(_roots[0][i - 1], _roots[1][i - 1]))
        i += 1

    global EULER
    EULER = np.copy(_roots, order='K')

    print("=========================================================================================================")
    print("\nEuler: ")
    getResult(_roots, 1)


def SmartEuler(y_0, h, a, b):
    _roots = [[0] * 1 for _ in range(3)]
    _roots[0][0] = a
    _roots[1][0] = y_0
    _roots[2][0] = y_0
    n = np.abs(a - b) / h + 1

    i = 1
    while i < n + 1:
        _roots[0].append(_roots[0][i - 1] + h)  # X
        _roots[1].append(_roots[1][i - 1] + h * function(_roots[0][i - 1], _roots[1][i - 1]))  # Предикатор
        _roots[2].append(_roots[2][i - 1] + (h / 2) * (
                function(_roots[0][i - 1], _roots[2][i - 1]) + function(_roots[0][i], _roots[1][i])))  # Корректор
        i += 1

    global SMART_EULER
    SMART_EULER = np.copy([_roots[0], _roots[2]], order='K')

    print("\n=========================================================================================================")
    print("\nSmartEuler: ")
    getResult(_roots, 2)


def Runge_Kutta(y_0, h, a, b):
    _roots = [[0] * 1 for _ in range(2)]
    _roots[0][0] = a
    _roots[1][0] = y_0
    n = np.abs(a - b) / h + 1

    k_1_4 = [0, 0, 0, 0]

    i = 1
    while i < n + 1:
        _roots[0].append(_roots[0][i - 1] + h)

        k_1_4[0] = function(_roots[0][i - 1], _roots[1][i - 1])
        k_1_4[1] = function(_roots[0][i - 1] + (h / 2), _roots[1][i - 1] + (h / 2 * k_1_4[0]))
        k_1_4[2] = function(_roots[0][i - 1] + (h / 2), _roots[1][i - 1] + (h / 2 * k_1_4[1]))
        k_1_4[3] = function(_roots[0][i - 1] + h, _roots[1][i - 1] + (h * k_1_4[2]))

        _roots[1].append(_roots[1][i - 1] + (h * (k_1_4[0] + 2 * k_1_4[1] + 2 * k_1_4[2] + k_1_4[3]) / 6))
        i += 1

    global ROOTS_RUNGE_KUTTA
    ROOTS_RUNGE_KUTTA = np.copy(_roots, order='K')

    global K_1_4
    K_1_4 = np.copy(k_1_4, order='K')

    print("\n=========================================================================================================")
    print("\nRunge-Kutta: ")
    getResult(_roots, 1)


def Adams(y_0, h, a, b):
    _roots = [[0] * 4 for _ in range(2)]
    _roots[0][0] = a
    _roots[1][0] = y_0

    for j in range(1, 3 + 1):
        _roots[0][j] = ROOTS_RUNGE_KUTTA[0][j]
        _roots[1][j] = ROOTS_RUNGE_KUTTA[1][j]

    n = np.abs(a - b) / h + 1
    i = 4
    while i < n + 1:
        _roots[0].append(_roots[0][i - 1] + h)
        _roots[1].append(_roots[1][i - 1] + h * (- 9 * function(_roots[0][i - 4], _roots[1][i - 4])
                                                 + 37 * function(_roots[0][i - 3], _roots[1][i - 3])
                                                 - 59 * function(_roots[0][i - 2], _roots[1][i - 2])
                                                 + 55 * function(_roots[0][i - 1], _roots[1][i - 1])) / 24)
        i += 1

    global ADAMS
    ADAMS = np.copy(_roots, order='K')

    print("\n=========================================================================================================")
    print("\nAdams: ")
    getResult(_roots, 1)


def main():
    """ Для ДУ по вариантам """
    # _h = 1 / 10
    # _a = 0.0
    # _b = 1.0
    # _y_0 = 2.0

    """ Для x - y """
    # _h = 1 / 2
    # _a = 0.0
    # _b = 2.0
    # _y_0 = 1.0

    """ Atta """
    _h = 1 / 5
    _a = 0
    _b = 1
    _y_0 = 1

    Euler(_y_0, _h, _a, _b)
    SmartEuler(_y_0, _h, _a, _b)

    print(K_1_4)

    Runge_Kutta(_y_0, _h, _a, _b)
    Adams(_y_0, _h, _a, _b)

    # print(ROOTS_RUNGE_KUTTA)

    draw_function(EULER, SMART_EULER, ROOTS_RUNGE_KUTTA, ADAMS)


if __name__ == '__main__':
    main()
