## module choleski
""" L = choleski(a)
    Choleski decomposition: [L][L]transpose = [a]

    x = choleskiSol(L,b)
    Solution phase of Choleski's decomposition method
"""
import numpy as np
import math
from Numerical_Methods.error import *


def choleski(a:float):
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = math.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k]))
        except ValueError:
            error.err('Matrix is not positive definite')
        for i in range(k + 1, n):
            a[i, k] = (a[i, k] - np.dot(a[i, 0:k], a[k, 0:k])) / a[k, k]
    for k in range(1, n): a[0:k, k] = 0.0
    return a


def choleskiSol(L:float, b:float):
    n = len(b)
    # Solution of [L]{y} = {b}
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k, 0:k], b[0:k])) / L[k, k]
    # Solution of [L_transpose]{x} = {y}
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(L[k + 1:n, k], b[k + 1:n])) / L[k, k]
    return b
