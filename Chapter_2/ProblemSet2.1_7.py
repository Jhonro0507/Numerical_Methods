import copy

import numpy as np
from Numerical_Methods.Rutines import LUdecomp
from Numerical_Methods.Rutines import choleski

A = np.array([[4., -1., 0.],
              [-1., 4., -1.],
              [0., -1., 4.]])
B = copy.copy(A)
LU_A = LUdecomp.LUdecomp(A)


# Doolittle’s decomposition
def doolittlesDecomp(A):
    tam = len(A)
    U = np.ones([tam, tam])
    L = np.ones([tam, tam])
    for i in range(tam):
        for j in range(tam):
            if j > i:
                U[i, j] = A[i, j]
                L[i, j] = 0
            elif j == i:
                U[i, j] = A[i, j]
            else:
                U[i, j] = 0
                L[i, j] = A[i, j]
    return U, L


[U, L] = doolittlesDecomp(LU_A)
print("Doolitle’s decomposition\nU=\n", U, "\nL=\n", L)

# Choleski’s decomposition
CholA = choleski.choleski(B)
print("\n Choleski’s decomposition\nL=\n", CholA)
