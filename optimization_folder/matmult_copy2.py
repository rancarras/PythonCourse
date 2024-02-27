import random
import numpy as np

N = 250
# NxN matrix
X = [[random.randint(0, 100) for _ in range(N)] for _ in range(N)]

# Nx(N+1) matrix
Y = [[random.randint(0, 100) for _ in range(N + 1)] for _ in range(N)]

# Use NumPy for matrix multiplication
@profile
def multi():
    result = np.dot(X, Y)

multi()

# If you want to print the result:
# print(result_list)
