n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

total = 0
arr = [0] * 10000

for i, j in zip(x, c):
    if j == 'G':
        arr[i] = 1
    else:
        arr[i] = 2

for m in range(10000 - k + 1):
    cnt = 0
    for n in range(m, m+k):
        cnt += arr[n]
    total = max(total, cnt)

print(total)