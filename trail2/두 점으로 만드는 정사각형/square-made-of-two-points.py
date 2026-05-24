# 첫 번째 직사각형의 두 점 입력
x1, y1, x2, y2 = map(int, input().split())

# 두 번째 직사각형의 두 점 입력
a1, b1, a2, b2 = map(int, input().split())

# 두 직사각형을 모두 포함하는 최소/최대 좌표 구하기
min_x = min(x1, a1)
max_x = max(x2, a2)
min_y = min(y1, b1)
max_y = max(y2, b2)

# 감싸는 데 필요한 가로 길이와 세로 길이 계산
width = max_x - min_x
height = max_y - min_y

# 정사각형이어야 하므로 둘 중 더 큰 값을 한 변의 길이로 선택
side = max(width, height)

# 정사각형의 최소 넓이 출력
print(side * side)