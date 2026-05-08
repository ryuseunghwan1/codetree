n = int(input())

arr_2d = [ [0 for _ in range(n) ] for _ in range(n)]

num = 1
cnt = 0
for i in range(n-1, -1, -1):
    if cnt % 2 == 0:
        for j in range(n-1, -1, -1):
            arr_2d[j][i] = num
            num += 1

        cnt += 1
    else:
        for m in range(n):
            arr_2d[m][i] = num
            num += 1

        cnt += 1

for s in arr_2d:
    for elem in s:
        print(elem, end=' ')
    print()
            