import numpy as np
from Numerical_Methods.Rutines.gaussElimin import gaussElimin
import conditioning
import rearrange
A = np.array([[0.,0.,2.,1.,2.],
              [0.,1.,0.,2.,-1.],
              [1.,2.,0.,-2.,0.],
              [0.,0.,0.,-1.,1.],
              [0.,1.,-1.,1.,-1.]])
b = np.array([[1.],
              [1.],
              [-4.],
              [-2.],
              [-1.]])
conditioning.conditioning(A,A)
A2 = rearrange.rearrange(A,b)
print("La matriz reordenada es:\n",A2)
x = gaussElimin(A,b)
print("El vector x que resuelve la ecuación Ax=b es:\n",x)
