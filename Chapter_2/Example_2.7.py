import numpy as np
from Numerical_Methods.Rutines.LUdecomp import *
a = np.array([[3.,-1.,4.],
              [-2.,0.,5.,],
              [7.,2.,-2.]])
b =np.array([[6.,-4.],
             [3.,2.],
             [7.,-5.]])
a = LUdecomp(a) # Decompose a
det = np.prod(np.diagonal(a))
print("\nDeterminant =",det)
for i in range(b.shape[1]):
    x = LUsolve(a,b[:,i])
    print("x",i+1,"=",x)
input("\nPress return to exit")