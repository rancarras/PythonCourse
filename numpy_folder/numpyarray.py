import numpy as np
import random

# Create a null vector of size 10
null_vector = np.zeros(10)

# Set the fifth value to 1
null_vector[4] = 1
print(null_vector)

# Create a vector with values ranging from 10 to 49
v1 = np.arange(10,50)
print(v1)
print("reversed numpy: ", np.flip(v1))
print("reversed slicing: ", v1[::-1])

# Create a 3x3 matrix with values ranging from 0 to 8.
m1 = [[0,1,2],[3,4,5],[6,7,8]]
m2 = np.arange(9).reshape(3,3)
print(m1, '\n', m2)

# Find indices of non-zero elements in the vector below
v2 = [1,2,0,0,4,0]
ar1 = np.nonzero(v2)[0]
print("Indices of the non-zero elements in vector v2: ", ar1)

# Create a random vector of size 30 and find the mean value
v3 = np.random.random((30))
avrg = np.average(v3)
print(avrg)

# Create a 2D array with 1 on the border and 0 inside
n = 10
toprow = np.ones(n)
middlerow = np.concatenate(([1], np.zeros((n-2), dtype=int), [1]))
midsection = np.tile(middlerow, (n-2,1))
m2 = np.vstack((toprow, midsection, toprow))
print(m2)

# Create a 8x8 matrix and fill it with a checkerboard pattern
checkerboard = np.full((8,8), 'o', dtype=str)
checkerboard[1::2, ::2] = 'x'
checkerboard[::2, 1::2] = 'x'
print(checkerboard)

# Create a checkerboard 8x8 matrix pattern using the tile function
n = 4
rowa = []
for i in range(n):
    rowa.append('o')
    rowa.append('x')

rowb = rowa[::-1]
checker = np.vstack((rowa,rowb))
checkerboard = np.tile((checker),(n,1))
print("checkerboard: ", '\n', checkerboard)

# Given a 1D array, negate all elements which are between 3 and 8, in place
z = np.arange(11)
z[(z>3) & (z<8)] *=- 1
print(z)

# Create a random vector of size 10 and sort it
z = np.random.random(10)
z = np.sort(z)
print(z)

# Consider two random array A and B, check if they are equal
a = np.random.randint(0,2,5)
b = np.random.randint(0,2,5)
equal = np.array_equal(a,b)
print(equal)

# How to calculate the square of every number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z **= 2
print(Z.dtype)

# How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D= np.diagonal(C)
print(D)
