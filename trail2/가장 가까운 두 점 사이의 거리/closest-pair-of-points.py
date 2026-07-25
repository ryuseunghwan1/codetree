n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()
print( ((points[1][0] - points[0][0]) ** 2) + ((points[1][1] - points[0][1]) ** 2)  ) 