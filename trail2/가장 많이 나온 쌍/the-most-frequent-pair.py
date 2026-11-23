n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

ans = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        
        cnt = 0
        for a, b in pairs:
            if ((a == i) and (b == j)) or ((a == j) and (b == i)):
                cnt += 1

        ans = max(ans, cnt)

print(ans)