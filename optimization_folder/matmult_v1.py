import random

@profile
def matrix_multiply(A, B):

    # Number of rows and columns for the result matrix
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])

    # Initialize result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]

    # Perform element-wise multiplication and summation
    for i in range(rows_A):
        for j in range(cols_B):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))

    return result

# Example usage
N = 250
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

    # Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

result_matrix = matrix_multiply(X,Y)
# print(result_matrix)