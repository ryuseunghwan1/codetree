N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    low = arr[i]
    high = low + K

    cnt = 0
    for j in arr:
        if low <= j <= high:
            cnt += 1

    ans = max(ans, cnt)

print(ans)