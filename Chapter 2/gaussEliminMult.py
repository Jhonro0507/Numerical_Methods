## module gaussElimin
""" x = gaussElimin(a,b).
    Solves [a][b] = [x] by Gauss elimination.
    Where all data in [a] and [b] should to be floating points
"""
import numpy as np

def gaussEliminMult(a: float, b: float):
    n = len(b[:,0])
    m = len(b[0,:])
  # Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
           if a[i,k] != 0.0:
               lam = a[i,k]/a[k,k]
               a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
               for p in range(0,m):
                   b[i,p] = b[i,p] - lam*b[k,p]
  # Back substitution
    for k in range(n-1,-1,-1):
        for p in range(0,m):
            b[k,p] = (b[k,p] - np.dot(a[k,k+1:n],b[k+1:n,p]))/a[k,k]
    return b
