import sys

INT_MAX = sys.maxsize

# 변수를 선언하고 입력을 받습니다.
n = int(input())
arr = list(map(int, input().split()))

min_dist = INT_MAX
# 각 i번째 집으로 모였을 때의 합을 구해줍니다.
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j - i) * arr[j]

    # 가능한 거리의 합 중 최솟값을 구해줍니다.
    min_dist = min(min_dist, sum_dist)

# 결과를 출력합니다.
print(min_dist)

