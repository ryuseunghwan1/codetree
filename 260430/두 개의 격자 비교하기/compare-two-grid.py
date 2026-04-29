a, b = map(int, input().split())
arr_1 = []
arr_2 = []

for _ in range(a):
    arr = list(map(int, input().split()))
    arr_1.append(arr)

for _ in range(a):
    arr = list(map(int, input().split()))
    arr_2.append(arr)

for i in range(a):
    for j in range(b):
        if arr_1[i][j] == arr_2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()