# -*- coding: utf-8 -*-
import numpy as np
from Rutines.gaussElimin import gaussElimin
from Chapter_2.conditioning import conditioning
def createPoly(x):
    n = len(x)
    A = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = x[i] ** j
    return A



x = np.array([0,1,3,5,6])*1.
A = createPoly(x)
print("Primero verifico condicionamiento\n")
conditioning(A, "A")
y = np.array([-1,1,3,2,-2])*1.
print("\nEl vector K que resuelve la ecuaicón A(x)K = y es:\n",gaussElimin(A, y))