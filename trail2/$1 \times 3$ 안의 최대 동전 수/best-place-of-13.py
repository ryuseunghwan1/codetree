n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0

# 모든 행(i)과 3칸 이상 확보할 수 있는 열(j)을 순회합니다.
for i in range(n):
    for j in range(n - 2):
        # 1 x 3 직사각형 범위 내의 동전 개수를 셉니다.
        current_coins = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        
        # 최대값 갱신
        if current_coins > max_coins:
            max_coins = current_coins

print(max_coins)