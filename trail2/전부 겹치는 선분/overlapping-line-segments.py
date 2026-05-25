n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

# 모든 선분의 시작점 중 가장 우측에 있는 점을 찾습니다.
max_x1 = max(x1)
# 모든 선분의 끝점 중 가장 좌측에 있는 점을 찾습니다.
min_x2 = min(x2)

# 가장 늦게 시작한 점이 가장 먼저 끝난 점보다 작거나 같다면 모든 선분이 겹치는 구간이 존재합니다.
if max_x1 <= min_x2:
    print("Yes")
else:
    print("No")