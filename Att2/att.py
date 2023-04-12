import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, Integral, exp, log
from threading import Thread
from scipy.special import roots_legendre

def function(x):
    f = 4 * np.sin(x * x) - np.log(x + 4)
    return f

def main():
    h = 1/6
    a = 1

    f0 = function(1)
    f1 = function(a + h)
    f2 = function(a + 2*h)
    f3 = function(a + 3*h)
    f4 = function(a + 4*h)
    f5 = function(a + 5*h)
    f6 = function(2)

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)

    print()

    print((1/18) * (f0 + 4 * (f1 + f3 + f5) + 2 * (f2 + f4) + f6))




if __name__ == '__main__':
    main()