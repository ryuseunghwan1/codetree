matrix = []

row = 3
col = 3
for i in range(row):
    new = []
    new_matrix = list(map(int, input().split()))
    
    for j in range(col):
        new.append(new_matrix[j]*3)
    matrix.append(new)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()