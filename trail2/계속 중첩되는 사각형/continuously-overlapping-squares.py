n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.


OFFSET = 100
grid = [ [0] * 205 for  _ in range(205)   ]

for i in range(n):
    if i % 2 == 0:
        start_x = x1[i] + OFFSET
        start_y = y1[i] + OFFSET
        end_x = x2[i] + OFFSET
        end_y = y2[i] + OFFSET

        for curr_x in range(end_x, start_x, -1):
            for curr_y in range(end_y, start_y, -1):
                grid[curr_x][curr_y] = 1

    else:
        start_x = x1[i] + OFFSET
        start_y = y1[i] + OFFSET
        end_x = x2[i] + OFFSET
        end_y = y2[i] + OFFSET

        for curr_x in range(end_x, start_x, -1):
            for curr_y in range(end_y, start_y, -1):
                grid[curr_x][curr_y] = 2
                
total_area = 0
for r in range(205):
    for c in range(205):
        if grid[r][c] == 2:
            total_area += 1

print(total_area)
                

        
