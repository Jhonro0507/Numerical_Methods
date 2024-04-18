# This example is [A]{x}={b} form
import numpy as np
from Numerical_Methods.Rutines.gaussElimin import gaussElimin
def vandermode(v:float):
    n = len(v)
    a = np.zeros((n,n))
    for j in range(n):
        a[:,j]=v**(n-j-1) # It's not necessary to express v positions explicitly because a[:,j] express it implicitly
    return a

v=np.array([1.,1.2,1.4,1.6,1.8,2.])
b=np.array([0.,1.,0.,1.,0.,1.])
a=vandermode(v)
aOrig=a.copy() # Save original a matrix
bOrig=b.copy() # Save original b vector
x=gaussElimin(a,b)
det=np.prod(np.diagonal(a))
print("x=\n",x)
print("\ndet(a)=",det)
print("\n a=",a)
print("\nChech result:[a]{x}-{b}=\n",np.dot(aOrig,x)-bOrig)
