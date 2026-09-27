import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

total = sum(a)

# 1번 방(인덱스 0)에서 시작할 때의 거리 합
cost = sum(a[i] * i for i in range(n))
best = cost

# 시작 방을 한 칸씩 옮기며 거리 합을 갱신
for s in range(n - 1):
    cost = cost - total + a[s] * n
    best = min(best, cost)

print(best)