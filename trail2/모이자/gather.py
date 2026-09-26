import sys

cnt = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))


for i in range(n):
    temp = 0

    for j in range(n):
        temp += abs(j - i) * arr[j]
    cnt = min(cnt, temp)

print(cnt)