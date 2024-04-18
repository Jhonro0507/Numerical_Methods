# -*- coding: utf-8 -*-
import numpy as np


def createPoly(x):
    n = len(x)
    A = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = x[i]**j
    return A


x =  np.array([0,0.75,)