n = int(input())

# 좌표가 -100부터 100까지이므로, 안전하게 200x200 크기의 격자를 0으로 초기화합니다.
# (음수 좌표를 양수로 바꾸기 위해 offset 100을 더해줄 것입니다)
OFFSET = 100
grid = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 음수 좌표를 양수 인덱스로 변환
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    # (x1, y1)부터 (x2, y2) 직사각형 면적 안의 격자 칸들을 1로 채웁니다.
    # 면적을 구하는 것이므로 이상/이하(<=)가 아니라 미만(<)까지 채워야 격자의 칸 개수와 넓이가 일치합니다.
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

# 격자에서 1로 칠해진 모든 칸의 개수를 세어 넓이를 구합니다.
total_area = 0
for row in grid:
    total_area += sum(row)

print(total_area)
