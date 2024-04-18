import numpy as np
import gaussEliminMult
A = np.array([[2.,0.,-1.,0.],
              [0.,1.,2.,0.],
              [-1.,2.,0.,1.],
              [0.,0.,1.,-2.]])
b = np.array([[1.,0.],
              [0.,0.],
              [0.,1.],
              [0.,0.]])
x = gaussEliminMult.gaussEliminMult(A,b)
print("El vector X que resuelve el sistema de ecuaciones Ax=b, es:\n",x)