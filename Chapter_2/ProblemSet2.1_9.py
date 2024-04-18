import numpy as np
import conditioning
from Numerical_Methods.Rutines import LUdecomp
from Numerical_Methods.Rutines import gaussElimin
A = np.array([[2.34, -4.10, 1.78],
              [-1.98, 3.47, -2.22],
              [2.36, -15.17, 6.18]])
b = np.array([[0.02],
              [-0.73],
              [-6.63]])
conditioning.conditioning(A, "A")
A_LU = LUdecomp.LUdecomp(A)
L = np.zeros([len(A_LU), len(A_LU)])
U = np.zeros([len(A_LU), len(A_LU)])
print(L)
for i in range(len(A_LU)):
    for j in range(len(A_LU)):
        if j > i:
            U[i, j] = A_LU[i, j]
            L[i, j] = 0
        elif i == j:
            L[i, j] = 1
            U[i, j] = A_LU[i, j]
        else:
            L[i, j] = A_LU[i, j]
            U[i, j] = 0
print("La matriz U es:\n")
print(U)
print("\nLa matriz L es:\n")
print(L)
# Como LUx=b, entonces Ux=y, Ly=b
# Primero resuelvo Ly=b
y = gaussElimin.gaussElimin(L, b)
print("\nEl vector Y que resuelve la ecuación LY=b es:\n")
print(y)
# Resuelvo Ux=y
x = gaussElimin.gaussElimin(U,y)
print("\nEl vector x que resuelve la ecuación Ux=y es:\n")
print(x)
