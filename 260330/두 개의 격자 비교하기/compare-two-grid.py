
row, col = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(row):
    new = []
    user = list(map(int, input().split()))
    for j in range(col):
        new.append(user[j])
    matrix_1.append(new)

for i in range(row):
    new = []
    user = list(map(int, input().split()))
    for j in range(col):
        new.append(user[j])
    matrix_2.append(new)

for i in range(row):
    for j in range(col):
        if matrix_1[i][j] == matrix_2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()