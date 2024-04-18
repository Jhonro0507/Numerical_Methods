from Numerical_Methods.Rutines.gaussElimin import gaussElimin
from gaussEliminMult import gaussEliminMult
import numpy as np
# Example 2.3
A = np.array([[6,-4,1],
              [-4,6,-4],
              [1,-4,6]])
B = np.array([[-14,22],
              [36,-18],
              [6,7]])
x=gaussEliminMult(A.astype(np.float_),B.astype(np.float_))
print(x)
