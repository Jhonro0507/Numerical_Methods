# Doolitles decomposition LUx=b
import numpy as np
import conditioning
from Numerical_Methods.Rutines import LUdecomp
from Numerical_Methods.Rutines import gaussElimin


def doolittlesDecomp(A):
    # This method is used after LUdecomp.LUdecomp
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
    print("Doolitles U matrix is:")
    print(U)
    print("\nDoolitles L matrix is:")
    print(L)
    return U, L


A = np.array([[4., -3., 6.],
              [8., -3., 10.],
              [-4., 12., -10.]])
b = np.array([[1., 0.],
              [0.,1.],
              [0., 0.]])
print("Primero verifico el condicionamiento:")
conditioning.conditioning(A,"A")
LU_A = LUdecomp.LUdecomp(A)
[U, L] = doolittlesDecomp(LU_A)
y = np.zeros(b.shape)
for i in range(b.shape[1]):
    y[:, i] = gaussElimin.gaussElimin(L, b[:, i])
print("\nLa matriz y que resuelve la ecuación Ly=b es:\n", y)
x = np.zeros(y.shape)
for i in range(y.shape[1]):
    x[:, i] = gaussElimin.gaussElimin(U, y[:, i])
print("\nLa matriz y que resuelve la ecuación Ux=y es:\n", x)
