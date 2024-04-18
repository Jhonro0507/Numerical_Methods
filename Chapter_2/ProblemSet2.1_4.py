import numpy as np
from Numerical_Methods.Rutines.gaussElimin import gaussElimin
A = np.array([[2.,-3.,-1.],
              [3.,2.,-5.],
              [2.,4.,-1.]])
b = np.array([[3.],
              [-9.],
              [-5.]])
x = gaussElimin(A,b)
print("El vector x que resuelve la ecuación Ax=b es:\n",x)