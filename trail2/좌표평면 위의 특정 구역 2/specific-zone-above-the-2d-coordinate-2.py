n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
cnt = 10000
for i in range(n):
    temp_x = []
    temp_y = []
    
    for j in range(n):
        if i == j:
            continue

        temp_x.append(points[j][0])
        temp_y.append(points[j][1])

    width = max(temp_x) - min(temp_x)
    height = max(temp_y) - min(temp_y)
    array = width * height
    
    cnt = min(array, cnt)

print(cnt)