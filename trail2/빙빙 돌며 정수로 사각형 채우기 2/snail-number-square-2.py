n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 방향 순서: 아래, 오른쪽, 위, 왼쪽
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r, c, d = 0, 0, 0       # 왼쪽 위에서 시작, 처음 방향은 아래
grid[r][c] = 1

for num in range(2, n * m + 1):
    nr, nc = r + dr[d], c + dc[d]   # 지금 방향으로 한 칸 앞

    # 격자를 벗어나거나 이미 채운 칸이면 방향을 바꿈
    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != 0:
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc
    grid[r][c] = num

for row in grid:
    print(*row)
    