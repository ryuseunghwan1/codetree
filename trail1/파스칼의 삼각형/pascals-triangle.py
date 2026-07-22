n = int(input())
arr_2d = [[0 for _ in range(n)] for _ in range(n) ]

for i in range(n):
    arr_2d[i][0] = 1


for j in range(1, n):
    for m in range(1, n):
        arr_2d[j][m] = arr_2d[j-1][m-1] + arr_2d[j-1][m]


for arr in arr_2d:
    for elem in arr:
        if elem > 0:
            print(elem, end=' ')
    print()