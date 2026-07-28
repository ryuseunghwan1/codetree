
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


max_area = 0

# 정확히 하나의 점을 제외하는 모든 경우의 수를 탐색
for i in range(n):
    temp_x = []
    temp_y = []
    
    for j in range(n):
        # i번째 점은 제외합니다.
        if i == j:
            continue
        
        temp_x.append(points[j][0])
        temp_y.append(points[j][1])
        
    # 남은 점들을 모두 포함하는 직사각형의 가로, 세로 길이 계산
    width = max(temp_x) - min(temp_x)
    height = max(temp_y) - min(temp_y)
    
    # 넓이 계산
    area = width * height % 2
    
    # 최소 넓이 갱신
    max_area = max(max_area, area)

print(max_area * 2)
        