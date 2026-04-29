a, b = map(int, input().split())

arr = [[0 for _ in range(b)]  for _ in range(a)]

cnt = 0
for i in range(a):
    for j in range(b):
        cnt += 1
        arr[i][j] = cnt

for m in arr:
    for n in m:
        print(n, end= ' ')
    print()
        