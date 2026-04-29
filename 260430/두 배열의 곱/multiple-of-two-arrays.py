arr_1 = []
arr_3 = []

for _ in range(3):
    arr = list(map(int, input().split()))
    arr_1.append(arr)


for _ in range(4):
    arr = list(map(int, input().split()))
    arr_3.append(arr)

arr_2 = arr_3[1:]

for i in range(3):
    for j in range(3):
        print(arr_1[i][j] * arr_2[i][j], end= ' ')
    print()