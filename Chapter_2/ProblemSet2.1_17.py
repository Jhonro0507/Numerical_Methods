# -*- coding: utf-8 -*-
import numpy as np
from Rutines import gaussElimin
from Chapter_2 import conditioning
A =  np.ones((4,4))
x = np.array([0.,1.,3.,4.])
for i in range(len(x)):
    for j in range(len(x)):
        A[i,j]= x[i] ** j
y = np.array([[10],
              [35],
              [31],
              [2]])*1.
print("Primero verifico condicionamiento\n")
conditioning.conditioning(A, "A")
print("\nEl vector K que resuelve la ecuación A(x)K = y es:\n", gaussElimin.gaussElimin(A, y))
