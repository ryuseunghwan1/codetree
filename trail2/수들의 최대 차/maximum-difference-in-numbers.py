N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if abs(arr[j] - arr[i]) <= K:
            cnt += 1

print(cnt)
        