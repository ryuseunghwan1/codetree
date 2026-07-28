n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

cnt = float('inf')
for i in range(n):
    for j in range(n):
        if i==j:
            continue

        x = abs(points[j][0] - points[i][0])
        y = abs(points[j][1] - points[i][1])

        multiple = (x ** 2) + (y ** 2)

        cnt  = min(multiple , cnt)

print(cnt)

        