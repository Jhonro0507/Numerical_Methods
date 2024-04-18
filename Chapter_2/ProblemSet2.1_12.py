# LUx=b
import numpy as np
import conditioning
from Numerical_Methods.Rutines import LUdecomp, gaussElimin


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



A = np.array([[4., -2., -3.],
               [12., 4., -10.],
               [-16., 28., 18.]])
b = np.array([[1.1],
               [0.],
               [-2.3]])
print("Primero verifico condicionamiento:")
conditioning.conditioning(A,"A")
LU_A = LUdecomp.LUdecomp(A)
[U, L] = doolittlesDecomp(LU_A)
print("\nEl vector Y que soluciona la euación LY=b es:\n")
y = gaussElimin.gaussElimin(L,b)
print(y)
print("\nEl vector x que resuelve la ecuación Ux=y es:\n")
print(gaussElimin.gaussElimin(U,y))
