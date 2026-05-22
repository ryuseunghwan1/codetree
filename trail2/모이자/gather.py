import sys

n = int(input())
A = list(map(int, input().split()))

# 최솟값을 구해야 하므로, 처음에는 아주 큰 값으로 초기화합니다.
min_total_distance = sys.maxsize

# i번째 집으로 모이는 모든 경우의 수를 시험해봅니다.
for i in range(n):
    current_distance_sum = 0
    
    # j번째 집에 있는 사람들이 i번째 집으로 이동합니다.
    for j in range(n):
        # (두 집 사이의 거리) * (j번째 집의 사람 수)
        current_distance_sum += abs(i - j) * A[j]
            
    # 매 경우마다 전체 이동 거리의 최솟값을 갱신합니다.
    min_total_distance = min(min_total_distance, current_distance_sum)

print(min_total_distance)

