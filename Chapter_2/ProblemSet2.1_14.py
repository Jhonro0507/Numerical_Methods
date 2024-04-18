#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:10:21 2023

@author: jhonatanromanroman
"""
import numpy as np
from Chapter_2.gaussEliminMult import gaussEliminMult

A = np.array([[2.,-1.,0.],
              [-1.,2.,-1.],
              [0.,-1.,2.]])
b = np.array([[1.,0.,0.],
              [0.,1.,0.],
              [0.,0.,1]])
x = gaussEliminMult(A, b)
print("La matriz X que resuelve la ecuación AX=b es:\n",x)
