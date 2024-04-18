#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:14:32 2023

@author: jhonatanromanroman
"""

import numpy as np
from Rutines import LUdecomp
import re


def HilbertMatrix(n):
    A = np.empty((n,n))
    for i in range (n):
        for j in range(n):
            if i==j :
                A[i,j]=1/(2*i+1)
            else :
                A[i,j]=1/(1+i+j)
    return A

def bFunction(A):
    b = np.empty((len(A)))*0.
    for i in range(len(A)):
        for j in range(len(A)):
            b[i] = b[i]+A[i,j]
    return b



print("Ingrese el valor de n:")
n = int(input())
A = HilbertMatrix(n)
b =  bFunction(A)
if n<5:
    print("\nLa Matriz de Hilbert es:\n",A)
    print("\nEl vector b es:\n",b)
A = LUdecomp.LUdecomp(A)
x = LUdecomp.LUsolve(A, b)
print("\n\nEl vector x que resuelve la ecuación Ax=b es:\n",x)


