a, b = map(int, input().split())

arr_2d = [[0 for _ in range(a)] for _ in range(a)]

for _ in range(b):
    r , c = tuple(map(int, input().split()))
    arr_2d[r-1][c-1] = 1

for i in arr_2d:
    for elem in i:
        print(elem, end=' ')
    print()    