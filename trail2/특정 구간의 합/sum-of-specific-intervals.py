n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

cnt = 0
for i, j in queries:
    for n in range(i, j+1):
        cnt += arr[n-1]
    print(cnt)
    cnt = 0


