n= int(input())

arr_2d = [[ 0 for _ in range(n) ] for _ in range(n)]

for i in range(n):
    arr_2d[0][i] = 1
    arr_2d[i][0] = 1

for j in range(1, 5):
    for m in range(1, 5):
        arr_2d[j][m] = arr_2d[j-1][m] + arr_2d[j][m-1] + arr_2d[j-1][m-1]

for arr in arr_2d:
    for elem in arr:
        print(elem, end=' ')
    print()