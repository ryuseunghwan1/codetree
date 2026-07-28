
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_area_times_2 = 0

# 1. N개의 점 중 3개의 점을 고르는 모든 조합을 완전탐색합니다.
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            
            # 2. 한 변은 x축에 평행 (y좌표가 같은 쌍이 존재해야 함)
            # 다른 한 변은 y축에 평행 (x좌표가 같은 쌍이 존재해야 함)
            if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
                # 직사각형의 넓이는 (가로 길이 * 세로 길이)
                # 문제에서 구하는 값은 '최대 넓이에 2를 곱한 값'이므로 
                # (가로 * 세로 * 2)에서 삼각형의 넓이 공식(/2)과 2가 상쇄되어 결국 (가로 * 세로)가 됩니다.
                width = max(abs(x1 - x2), abs(x2 - x3), abs(x1 - x3))
                height = max(abs(y1 - y2), abs(y2 - y3), abs(y1 - y3))
                
                area_times_2 = width * height
                max_area_times_2 = max(max_area_times_2, area_times_2)

print(max_area_times_2)