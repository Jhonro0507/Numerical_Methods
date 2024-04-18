import numpy as np
La = np.array([[1.,0.,0.],
               [1.,1.,0.],
               [1.,5/3,1]])
Ua = np.array([[1.,2.,4.],
              [0.,3.,21.],
              [0.,0.,0.]])
A = np.dot(La,Ua)
print("La matriz A, del punto a es:\n",A)
print("El determinante de la matriz A del punto a, es:", np.linalg.det(A))
Lb = np.array([[2.,0.,0.],
              [-1.,1.,0.],
              [1.,-3.,1]])
Ub = np.array([[2.,-1.,1.],
               [0.,1.,-3.],
               [0.,0.,1.]])
B = np.dot(Lb,Ub)
print("La matriz A, del punto a es:\n",B)
print("El determinante de la matriz A del punto b, es:", np.linalg.det(B))