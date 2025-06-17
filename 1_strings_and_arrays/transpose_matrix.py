# Problem: Transpose Matrix: 

# Write a function transpose() that accepts a 2D integer array matrix and returns
# the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, 
# swapping the rows and columns.

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[j][i]

    return result

# Tests

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix1))

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix2))

