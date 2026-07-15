matrix = [[1,2,0],[3,0,2],[3,0,1]]

n = 3

def col_reduction(matrix):
    for i in range(n):
        min = 100000000000
        j = 0
        tri = 0
        while j < n: 
            if min > matrix[j][i]:
                min = matrix[j][i]
            

            if j == n-1 and tri == 0:
                j = -1
                tri += 1
            elif tri != 0:
                matrix[j][i] = matrix[j][i] - min

            j+=1

    return matrix

zero = {}

for i in range(3):
    zero[i] = []
    for j in range(3):
        zero[i].append(j)

print(zero)