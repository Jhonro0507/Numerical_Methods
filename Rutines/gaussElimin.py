## module gaussElimin
""" x = gaussElimin(a,b).
    Solves [a]{b} = {x} by Gauss elimination.
    Where all data in [a] and {b} should to be floating points
"""
import numpy as np

def gaussElimin(a:float,b:float):
    n = len(b)
    a = a
  # Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
           if a[i,k] != 0.0:
               lam = a[i,k]/a[k,k]
               a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
               b[i] = b[i] - lam*b[k]
  # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
