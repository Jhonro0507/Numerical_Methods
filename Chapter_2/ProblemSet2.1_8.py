# Doolitles decomposition LUx=b
import numpy as np
from Numerical_Methods.Rutines import LUdecomp
from Numerical_Methods.Rutines import gaussElimin
import conditioning


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
    return U, L


A = np.array([[-3., 6., -4.],
              [9., -8., 24.],
              [-12., 24., -26.]])
b = np.array([[-3.],
              [65.],
              [-42.]])
print("Primero verifico el condicionamiento")
conditioning.conditioning(A,"A")
LU_A = LUdecomp.LUdecomp(A)
[U, L] = doolittlesDecomp(LU_A)
print("\nDoolitle's decomposition of A matrix is:\n")
print("U = ")
print(U)
print("L = ")
print(L)
print("\n El vector Y que resuelve la ecuación LY=b es:")
y = gaussElimin.gaussElimin(L,b)
print("\n y = ", y)
print("\n El vector x que resuelve la ecuación Ux=y es:")
print("\n x = ", gaussElimin.gaussElimin(U,y))
