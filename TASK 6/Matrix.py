matrix = [[0 for _ in range(3)] for _ in range(2)]

def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(input(f"Enter value for position [{i}][{j}]: "))

def print_matrix(matrix):
    print("\nMatrix:")
    for row in matrix:
        for col in row:
            print(col, end=" ")    
        print()

def matrix_transpose(matrix):
    transposed = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed[j][i] = matrix[i][j]
    return transposed

fill_matrix(matrix)
print_matrix(matrix)
transposed_matrix = matrix_transpose(matrix)
print("\nTransposed Matrix:")
print_matrix(transposed_matrix)
