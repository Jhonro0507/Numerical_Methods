import numpy as np
from Numerical_Methods.Rutines import gaussElimin
L = np.array([[1.,0.,0.],
              [3/2.,1.,0.],
              [1/2.,11/13.,1.]])
U = np.array([[2.,-3.,-1.],
              [0.,13/2.,-7/2.],
              [0.,0.,32/13.]])
b = np.array([[1.],
              [-1.],
              [2.]])
A = np.dot(L,U)
print("La matriz A=LU es:\n",A)
# Ax=b -> LUx=b donde (Ux)=y -> 1.Ly=b despejo "y"
# Resuelvo Ly=b
y = gaussElimin.gaussElimin(L,b)
print("La matriz 'y' resultado de Ly=b es:\n",y)
# Para Ux=y
x = gaussElimin.gaussElimin(U,y)
print("La matriz 'x' resultado de Ux=y es:\n",y)