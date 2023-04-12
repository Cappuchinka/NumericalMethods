import numpy as np
from threading import Thread


def is_exit(x, y, z, nx, ny, nz, eps):
    return np.abs(x - nx) < eps and np.abs(y - ny) < eps and np.abs(z - nz) < eps


def Jacobi(e_m, eps):
    _roots = [[0] * len(e_m[0]) for _ in range(len(e_m))]

    i = 1
    while True:
        _x = (1 / e_m[0][0]) * (e_m[0][3] - e_m[0][1] * _roots[1][i - 1] - e_m[0][2] * _roots[2][i - 1])
        _roots[0].append(_x)

        _y = (1 / e_m[1][1]) * (e_m[1][3] - e_m[1][0] * _roots[0][i - 1] - e_m[1][2] * _roots[2][i - 1])
        _roots[1].append(_y)

        _z = (1 / e_m[2][2]) * (e_m[2][3] - e_m[2][0] * _roots[0][i - 1] - e_m[2][1] * _roots[1][i - 1])
        _roots[2].append(_z)

        if is_exit(_roots[0][i], _roots[1][i], _roots[2][i],
                   _roots[0][i - 1], _roots[1][i - 1], _roots[2][i - 1], eps):
            break
        i += 1

    _last_results_id = len(_roots[0])
    _result = []
    for i in range(3):
        _result.append(_roots[i][_last_results_id - 1])

    print("\nResult Jacobi: ")
    print(_result)


def Seidel(e_m, eps):
    _roots = [[0] * len(e_m[0]) for _ in range(len(e_m))]

    i = 1
    while True:
        _x = (1 / e_m[0][0]) * (e_m[0][3] - e_m[0][1] * _roots[1][i - 1] - e_m[0][2] * _roots[2][i - 1])
        _roots[0].append(_x)

        _y = (1 / e_m[1][1]) * (e_m[1][3] - e_m[1][0] * _roots[0][i] - e_m[1][2] * _roots[2][i - 1])
        _roots[1].append(_y)

        _z = (1 / e_m[2][2]) * (e_m[2][3] - e_m[2][0] * _roots[0][i] - e_m[2][1] * _roots[1][i])
        _roots[2].append(_z)


        if is_exit(_roots[0][i], _roots[1][i], _roots[2][i],
                   _roots[0][i - 1], _roots[1][i - 1], _roots[2][i - 1], eps):
            break
        i += 1

    _last_results_id = len(_roots[0])
    _result = []
    for i in range(3):
        _result.append(_roots[i][_last_results_id - 1])

    print("\nResult Seidel: ")
    print(_result)


def main():
    _extended_matrix = np.array([[5.0, -1.0, 3.0, -3.0],
                                 [-4.0, 6.0, -1.0, 4.0],
                                 [-3.0, 3.0, 7.0, -11.0]])

    _eps = 0.000000000000001

    print("Matrix A: ")
    for i in range(3):
        for j in range(3):
            print(_extended_matrix[i][j], end=' ')
        print()

    print("\nMatrix B: ")

    for i in range(3):
        print(_extended_matrix[i][3])

    Jacobi(_extended_matrix, _eps)
    Seidel(_extended_matrix, _eps)

    # thread1 = Thread(target=Seidel, args=(_extended_matrix, _eps))
    # thread2 = Thread(target=Jacobi, args=(_extended_matrix, _eps))
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()


if __name__ == '__main__':
    main()
