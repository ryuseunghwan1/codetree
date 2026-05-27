x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

OFFSET = 1000
grid = [[0] * 2005 for _ in range(2005)]

# 1. 첫 번째 사각형 영역을 1로 채우기
start_x1, start_y1 = x1[0] + OFFSET, y1[0] + OFFSET
end_x1, end_y1 = x2[0] + OFFSET, y2[0] + OFFSET

for curr_x in range(start_x1, end_x1):
    for curr_y in range(start_y1, end_y1):
        grid[curr_x][curr_y] = 1

# 2. 두 번째 사각형 영역을 0으로 지우기
start_x2, start_y2 = x1[1] + OFFSET, y1[1] + OFFSET
end_x2, end_y2 = x2[1] + OFFSET, y2[1] + OFFSET

for curr_x in range(start_x2, end_x2):
    for curr_y in range(start_y2, end_y2):
        grid[curr_x][curr_y] = 0

# 3. 1로 채워져 있는 칸들의 '최소/최대 x, y 좌표' 구하기
min_x, max_x = 2005, -1
min_y, max_y = 2005, -1
exist_debris = False  # 잔해물이 남아있는지 체크하는 변수

for curr_x in range(2005):
    for curr_y in range(2005):
        if grid[curr_x][curr_y] == 1:
            exist_debris = True
            # 최솟값, 최댓값 갱신
            if curr_x < min_x: min_x = curr_x
            if curr_x > max_x: max_x = curr_x
            if curr_y < min_y: min_y = curr_y
            if curr_y > max_y: max_y = curr_y

# 4. 덮을 수 있는 최소 면적 계산하기
if not exist_debris:
    # 두 번째 사각형이 첫 번째 사각형을 완전히 다 덮어버린 경우
    print(0)
else:
    # 사각형의 가로, 세로 길이는 (최대 좌표 - 최소 좌표 + 1) 입니다.
    # (예: 인덱스 2번부터 5번까지 채워져 있다면 길이는 5 - 2 + 1 = 4칸)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)