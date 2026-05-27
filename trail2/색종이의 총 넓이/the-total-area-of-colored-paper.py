n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# 1. 음수 좌표 처리를 위한 OFFSET 설정 및 격자 크기 선언
# 좌표 -100 ~ 100을 0 ~ 200으로 변환하기 위해 100을 더해줍니다.
OFFSET = 100
grid = [[0] * 205 for _ in range(205)]

# 2. 각 색종이의 좌측 하단 좌표부터 가로 8, 세로 8 크기만큼 격자 칠하기
for i in range(n):
    # OFFSET을 더해 음수 좌표를 양수 인덱스로 변환
    start_x = x[i] + OFFSET
    start_y = y[i] + OFFSET
    
    # 가로 8, 세로 8 영역을 반복문으로 돕니다.
    for curr_x in range(start_x, start_x + 8):
        for curr_y in range(start_y, start_y + 8):
            grid[curr_x][curr_y] = 1 # 색종이가 놓인 영역을 1로 표시

# 3. 격자에서 1로 채워진 영역의 총 넓이(개수) 구하기
total_area = 0
for r in range(205):
    for c in range(205):
        if grid[r][c] == 1:
            total_area += 1

print(total_area)