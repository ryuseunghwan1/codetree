n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
arr= []
for i in range(n):
    for j in range(2):
        if points[i][1][j] < 0:
            arr.append(-(points[i][1][j]))
        else:
            arr.append(points[i][1][j])

