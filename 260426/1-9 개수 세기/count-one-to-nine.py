N = int(input())
arr = list(map(int, input().split()))
cnt = [0 for _ in range(9)]
for i in arr:
    cnt[i-1] += 1

for j in cnt:
    print(j)