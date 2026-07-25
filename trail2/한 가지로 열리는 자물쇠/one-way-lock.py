n = int(input())
a, b, c = map(int, input().split())

cnt = n ** 3
for i in range(1, n+1):
    for j in range(1, n+1):
        for m in range(1, n+1):
            if (i - a >= 3) and (j-b >= 3) and (m-c >=3):
                cnt -= 1                

print(cnt)