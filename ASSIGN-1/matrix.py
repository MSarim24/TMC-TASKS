r = int(input("Enter the number of the rows: "))
c = int(input("Enter the number of the cols: "))

matrix = [[int(input("Enter the value:"))for _ in range(c)] for _ in range(r)]

def validate_suquare_matrix(matrix):
    r= len(matrix)
    c= len(matrix[0])
    if  r == c :
        return matrix
    else:
        new_matrix = [[0 for _ in range(max(r,c))]for _ in range(max(r,c))]
        for i in range(max(r,c)):
            for j in range(max(r,c)):
                try:
                    new_matrix[i][j] = matrix[i][j]
                except:
                    new_matrix[i][j] = 0

        matrix = new_matrix

    return matrix
        
def print(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end="  ")
        print()

matrix = validate_suquare_matrix(matrix)
nums = [i for i in range(len(matrix))]
used = [0 for _ in range(len(matrix))]
perms = []
output = [0] * len(matrix)
n = len(matrix)

def permutaions(pos):
    if pos == len(matrix):
        perms.append(output.copy())
        return
    for i in range(len(matrix)):
        if used[i] == 0:
            output[pos] = nums[i]
            used[i] = 1

            permutaions(pos+1)

            used[i] = 0
   
def brute_force(matrix):
    max = 0
    best = None
    permutaions(0)
    
    for perm in perms:
        total_cost = 0

        for i in range(n):
            total_cost += matrix[i][perm[i]]

        if max < total_cost:
            max = total_cost
            best = perm

    return best 

best = brute_force(matrix)
new_matrix = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    new_matrix[i][best[i]] = 1



#---------- HUNGARIAN MAETHOD ------------


def find_max(matrix):
    max = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > max:
                max = matrix[i][j]
    return max
            

def convert_matrix(matrix):
    max = find_max(matrix)
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = max - matrix[i][j]

def row_reduction(matrix):
    for i in range(n):
        min = 100000000000
        j = 0
        tri = 0
        while j < n: 
            if min > matrix[i][j]:
                min = matrix[i][j]
            

            if j == n-1 and tri == 0:
                j = -1
                tri += 1
            elif tri != 0:
                matrix[i][j] = matrix[i][j] - min

            j+=1

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


num_of_Zeros_per_row = []
bipartite_graph = {}
best = [-1 for i in range(n)] 


def zero_s(matrix):
    for i in range(n):
        zeros = 0
        bipartite_graph[i] = []
        for j in range(n):
            if matrix[i][j] == 0:
                zeros += 1
                bipartite_graph[i].append(j)
        num_of_Zeros_per_row.append([zeros,i])

    num_of_Zeros_per_row.sort()

def max_matching(matrix, row, visited):
     
    for col in bipartite_graph[row]:
        if visited[col]:
            continue

        visited[col] = True
        if best[col] == -1:
            best[col] = row
            return True

       
        owner = best[col]

        if max_matching(matrix, owner, visited):
            best[col] = row
            return True

    return False



def find_maximum_matching(matrix):
    global best
    
    num_of_Zeros_per_row.clear()
    bipartite_graph.clear()
    zero_s(matrix)
    best = [-1] * n

    matches = 0

    for _,row in num_of_Zeros_per_row:
        visited = [False] * n

        if max_matching(matrix,row,visited):
            matches += 1

    return matches, best

