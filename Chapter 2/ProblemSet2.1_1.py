import numpy as np
import conditioning


a = np.array([[1., 2., 3.],
              [2., 3., 4.],
              [3., 4., 5.]])
conditioning.conditioning(a,"a")

b = np.array([[2.11, -0.8, 1.72],
              [-1.84, 3.03, 1.29],
              [-1.57, 5.25, 4.3]])
conditioning.conditioning(b,"b")

c = np.array([[2.,-1.,0.],
              [-1.,2.,-1.],
              [0.,-1.,2.]])
conditioning.conditioning(c,"c")

d = np.array([[4.,3.,-1.],
              [7.,-2.,3.],
              [5.,-18.,13.]])
conditioning.conditioning(d,"d")

