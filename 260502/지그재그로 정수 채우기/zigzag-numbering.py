a, b = map(int, input().split())

# Please write your code here.

cnt = 0
arr = [[ 0 for _ in range(b)] for _ in range(a)]

cnt = 0
arr = [[ 0 for _ in range(b)] for _ in range(a)]

for i in range(b):
    if i % 2 == 0:
        for j in range(a):
            arr[j][i] = cnt
            cnt += 1
    else:
        for m in range(a-1, -1, -1):
            arr[m][i] = cnt
            cnt += 1

for m in arr:
    for n in m:
        print(n, end = ' ')
    print()
