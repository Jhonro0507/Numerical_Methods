# LUx=b
import numpy as np
from Numerical_Methods.Rutines import choleski
from Numerical_Methods.Rutines import gaussElimin
import conditioning
A = np.array([[1.,1.,1.],
              [1.,2.,2.],
              [1.,2.,3.]])
b = np.array([[1.],
              [3/2.],
              [3.]])
L = choleski.choleski(A)
print("Verifico condicionamiento:")
conditioning.conditioning(A,"A")
print("\nLa descomposición de A según Choleski ( L=transpose(U) ) es:\n", L)
U = L.transpose()
print("\nPor lo tanto, la matriz U sería:\n", U)
y = gaussElimin.gaussElimin(L, b)
print("\nLa matriz Y que resuelve la ecuación LY=b es:\n", y)
x = gaussElimin.gaussElimin(U,y)
print("\nLa matriz x que resuelve la ecuación Ux=y es:\n",x)
