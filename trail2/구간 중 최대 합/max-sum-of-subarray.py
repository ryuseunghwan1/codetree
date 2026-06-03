n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

total = 0

for i in range(n-k+1):
    cnt = 0
    for j in range(i, i+k):
        cnt += arr[j]
    total = max(total, cnt)

print(total)
    