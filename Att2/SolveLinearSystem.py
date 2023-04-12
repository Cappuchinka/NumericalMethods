import numpy as np
from threading import Thread

import numpy.linalg


def Gauss(e_m):
    e_m_c = np.copy(e_m, order='K')
    n = len(e_m)

    """ Прямой ход """
    for k in range(n):
        for i1 in range(n + 1):
            e_m_c[k][i1] = e_m_c[k][i1] / e_m[k][k]
        for i1 in range(k + 1, n):
            coef1 = e_m_c[i1][k] / e_m_c[k][k]
            for j in range(n + 1):
                e_m_c[i1][j] = e_m_c[i1][j] - coef1 * e_m_c[k][j]
        for i1 in range(n):
            for j in range(n + 1):
                e_m[i1][j] = e_m_c[i1][j]

    """ Обратный ход """
    k = n - 1
    while k > -1:
        i1 = n
        while i1 > -1:
            e_m_c[k][i1] = e_m_c[k][i1] / e_m[k][k]
            i1 -= 1

        i2 = k - 1
        while i2 > -1:
            coef2 = e_m_c[i2][k] / e_m_c[k][k]
            j = n
            while j > -1:
                e_m_c[i2][j] = e_m_c[i2][j] - coef2 * e_m_c[k][j]
                j -= 1
            i2 -= 1
        k -= 1

    """ Получение решения """
    solve = []
    for i in range(n):
        solve.append(e_m_c[i][n])

    print("\nResult Gauss: ")
    print(solve)


def is_exit(x, y, z, w, nx, ny, nz, nw, eps):
    return np.abs(x - nx) < eps and np.abs(y - ny) < eps and np.abs(z - nz) and np.abs(w - nw) < eps


def Jacobi(e_m, eps):
    _roots = [[0] * len(e_m[0]) for _ in range(len(e_m))]

    i = 1
    while True:
        _x = (1 / e_m[0][0]) * (e_m[0][4] - e_m[0][1] * _roots[1][i - 1] - e_m[0][2] * _roots[2][i - 1] -
                                e_m[0][3] * _roots[3][i - 1])
        _roots[0].append(_x)

        _y = (1 / e_m[1][1]) * (e_m[1][4] - e_m[1][0] * _roots[0][i - 1] - e_m[1][2] * _roots[2][i - 1] -
                                e_m[1][3] * _roots[3][i - 1])
        _roots[1].append(_y)

        _z = (1 / e_m[2][2]) * (e_m[2][4] - e_m[2][0] * _roots[0][i - 1] - e_m[2][1] * _roots[1][i - 1] -
                                e_m[2][3] * _roots[3][i - 1])
        _roots[2].append(_z)

        _w = (1 / e_m[3][3]) * (e_m[3][4] - e_m[3][0] * _roots[0][i - 1] - e_m[3][1] * _roots[1][i - 1] -
                                e_m[3][2] * _roots[2][i - 1])
        _roots[3].append(_w)

        if is_exit(_roots[0][i], _roots[1][i], _roots[2][i], _roots[3][i],
                   _roots[0][i - 1], _roots[1][i - 1], _roots[2][i - 1], _roots[3][i - 1], eps):
            break
        i += 1

    _last_results_id = len(_roots[0])
    _result = []
    for i in range(4):
        _result.append(_roots[i][_last_results_id - 1])

    print("\nResult Jacobi: ")
    print(_result)


def Seidel(e_m, eps):
    _roots = [[0] * len(e_m[0]) for _ in range(len(e_m))]

    i = 1
    while True:
        _x = (1 / e_m[0][0]) * (e_m[0][4] - e_m[0][1] * _roots[1][i - 1] - e_m[0][2] * _roots[2][i - 1] -
                                e_m[0][3] * _roots[3][i - 1])
        _roots[0].append(_x)

        _y = (1 / e_m[1][1]) * (e_m[1][4] - e_m[1][0] * _roots[0][i] - e_m[1][2] * _roots[2][i - 1] -
                                e_m[1][3] * _roots[3][i - 1])
        _roots[1].append(_y)

        _z = (1 / e_m[2][2]) * (e_m[2][4] - e_m[2][0] * _roots[0][i] - e_m[2][1] * _roots[1][i] -
                                e_m[2][3] * _roots[3][i - 1])
        _roots[2].append(_z)

        _w = (1 / e_m[3][3]) * (e_m[3][4] - e_m[3][0] * _roots[0][i] - e_m[3][1] * _roots[1][i] -
                                e_m[3][2] * _roots[2][i])
        _roots[3].append(_w)

        if is_exit(_roots[0][i], _roots[1][i], _roots[2][i], _roots[3][i],
                   _roots[0][i - 1], _roots[1][i - 1], _roots[2][i - 1], _roots[3][i - 1], eps):
            break
        i += 1

    _last_results_id = len(_roots[0])
    _result = []
    for i in range(4):
        _result.append(_roots[i][_last_results_id - 1])

    print("\nResult Seidel: ")
    print(_result)


def main():
    _extended_matrix = np.array([[100, 0, 84, -142],
                                 [0, 18, -30, -12],
                                 [84, -30, 122, 20]])

    a = [[100, 0, 84], [0, 18, -30], [84, -30, 122]]
    b = [-142, -12, 20]
    _eps = 0.000000000000001

    print(np.linalg.solve(a, b))


if __name__ == '__main__':
    main()
