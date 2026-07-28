n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def calculate(a,b):
    total = b - a
    return total

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        first = calculate(points[i][0], points[i][1])
        second = calculate(points[j][0], points[j][1])
        total = first + second

        cnt = max(total, cnt)

print(cnt-1)

        