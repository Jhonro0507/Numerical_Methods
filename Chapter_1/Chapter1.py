## 1.2 Core Python
# Variables: python is typed dynamically
b = 2 # b is int type
print(b)
b = b*2.0 # now b is float type
print(b)

# Strings
string1 = "Press return to exit"
string2 = "the program"
print(string1+" "+string2) # Concatenation
print(string1[0:12]) # Slicing
s = "3 9 81"
print(s.split()) # Split s objet in its component parts where delimiter is white space
s[0] = "0" # It returns an error due String objects are immutable

# Tuples: ARE NOT MUTABLE, enclosed in parentheses
rec = ("Smith", "John", (6,23,68)) #This is a tuple
lastName, firstName, birthDate = rec #Unpacking the tuple
print(firstName)
birthYear = birthDate[2]
print(birthYear)
name = rec[1]+" "+rec[0]
print(name)
print(rec[0:2])

# Lists: ARE MUTABLE, enclosed in brackets
a = [1.0, 2.0, 3.0] # Create a list
a.append(4.0) # Append 4.0 to list
print(a)
a.insert(0,0.0) # insert 0.0 in position 0
print(a)
print(len(a)) # Determine length of list
a[2:4] = [1.0, 1, 1] # Modify selected elements
print(a)
b = a # b is an alias of a
b[0] = 5 # as b = a, b[0]=a[0]=5
print(a)
c = a[:] # c is an independent copy of a
c[0] = 1
print(a) # a is not affected by the change
a =[[1,2,3],\
    [4,5,6],\
    [7,8,9]] # Matrices are represented as nested lists
print(a[0]) # first raw of a
print(a[1][2]) # second raw and third element in a

# Arithmetic Operators
s = "Hello"
t = "to you"
a = [1,2,3]
print(3*s) # Repetition
print(3*a) # Repetition
print(a+[4,5]) # Append elements
print(s+" "+t) # Concatenation
print(3+s) # This adition has no sense

# Comparison operators
a = 2 # Integer
b = 1.99 # Floating point
c = "2" # String
print(a>b)
print(a==c)
print((a>b)and(a!=c))
print((a>b)or(a==b))

# Conditionals
def sign_of_a(a):
    if a < 0.0:
        sign= "negative"
    elif a>0.0:
        sign= "positive"
    else:
        sign= "zero"
    return sign
a = 1.5
print("a is "+sign_of_a(a))


# Loops
# While
nMax=5
n=1
a=[] # Create empty list
while n<nMax:
    a.append(1.0/n) # Append element to list
    n+=1
print(a)

# For
nMax=6
a=[]
for n in range(1,nMax):
    a.append(1/n)
print(a)

# Break use
list=["Jack", "Jill", "Tim", "Dave"]
name=eval(input("Type name: ")) # Python input prompt
for i in range(len(list)):
    if list[i]==name:
        print(name, " is number ", i+1, "on the list")
    break # We use break because we don’t write else command

# Continue use
x=[] # Create an empty list
for i in range(1,100):
    if i%7 != 0:
        continue
    else:
        x.append(i)
print(x)

# Type Conversion
a=5
b=-3.6
d="4.0"
print(a+b)
print(int(b))
print(complex(a,b))
print(float(d))
print(int(d))

# Mathematical functions
abs(-3)
max([1,2,3,1])
min([1,2,3,1])
round(3.5678,2)

# Reading input
a=input("Input a:")
print(a, type(a))
b=eval(a)
print(b, type(b))
a=eval(input("Input a:"))
print(a, type(a))



# 1.3 Functions
def derivatives(f,x,h=0.0001):
    df=(f(x+h)-f(x-h))/(2*h)
    dff=(f(x+h)-2*f(x)+f(x-h))/h**2
    return df,dff
from math import atan
df,dff=derivatives(atan, 0.5)
print("First derivative =",df)
print("Secondo derivative =",dff)
def prueba(x1,x2,*x3):
    print(x1,"y",x2, "are positional parameters")
    for i in range(len(x3)):
        print(x3[i], "is a excess parameter")
prueba(1,2,3,4,5,6,7)
# Lambda Statement
c=lambda x,y:x**2+y**2
print(c(5,2))



# 1.4 Mathematics Modules
# math Module
import math
print(math.log(math.sin(0.5)))
import math as m # import under an alias
print(m.log(m.sin(0.5)))
dir(math)
# Creating an array
from numpy import array
a=array([[2.0, -1.0],[-1.0,3.0]])
print(a)
b=array([[2,-1],[-1,3]],float)
print(b)
from numpy import *
print(arange(2,10,2))
print(arange(2.0,10.0,2.0))
print(zeros(2))
print(zeros((3), int))
print(ones((2,2)))

#Accesing and changing Array Elements
a=zeros((3,3),int)
print(a)
a[0]=[2,3,2] # Change a row
a[1,1]=5
a[2,0:2]=[8,-3]
print(a)

#Operations on Arrays
from numpy import array
a=array([0.0,4.0,9.0,16.0])
print(a/16)
print(a-4)
from numpy import array, sqrt, sin
a = array([1.0, 4.0, 9.0, 16.0])
print(sqrt(a))

# Array Functions
import numpy as np
A = np.array([[4,-2,1],[-2,4,-2],[1,-2,3]],float)
b = np.array([1,4,3],float)
np.diagonal(A)
print(np.diagonal(A))
print(np.trace(A))
print(np.argmax(b)) # index max argument
print(np.argmin(A, axis=0)) # index of smallest col. elements
print(np.identity(3))

x=np.array([7,3])
y=np.array([2,1])
A=np.array([[1,2],[3,2]])
B=np.array([[1,1],[2,2]])
# Dot product
print("dot(x,y) = \n",np.dot(x,y)) # {x}.{y}
print("dot(A,x) = \n", np.dot(A,x)) # [A]{x}
print("dot(A,B) =\n", np.dot(A,B)) # [A][B]
# Inner product
print("inner(x,y) =\n", np.inner(x,y)) # {x}.{y}
print("inner(A,x) =\n", np.inner(A,x)) # [A]{x}
print("inner(A,B) =\n", np.inner(A,B)) # [A][B_transpose]
# Outer product
print("outer(x,y) =\n", np.outer(x,y)) # {x_transpose}.{y}
print("outer(A,x) =\n", np.outer(A,x))
print("outer(A,B) =\n", np.outer(A,B))

# Linear Algebra Module
A=np.array([[4.0,-2.0,1.0],
            [-2.0,4.0,-2.0],
            [1.0,-2.0,3.0]])
b=np.array([1.0,4.0,2.0])
print(np.linalg.inv(A)) # A inverse
print(np.linalg.solve(A,b)) # Solve [A]{x}={b}

# Copying Arrays
c = b.copy() # deep copy

# Plotting with matplotlib.pyplot
# One plot
import matplotlib.pyplot as plt
x=np.arange(0.0,6.2,0.2)
plt.plot(x,np.sin(x),"o-",x,np.cos(x),"^-")
plt.xlabel("x")
plt.legend(("sine","cosine"),loc=0)
plt.grid(True)
plt.savefig("testplot.png",format="png")
plt.show()
# Multiple plot
x = np.arange(0.0,6.2,0.2)
plt.subplot(2,1,1) # subplot(rows, cols, plot_number)
plt.plot(x,np.sin(x),"o-")
plt.xlabel("x");plt.ylabel("sin(x)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,np.cos(x),"^-")
plt.xlabel("x"); plt.ylabel("cos(x)")
plt.grid(True)
plt.show()
