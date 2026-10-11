n, m = map(int, input().split())
grid = [[''] * m for _ in range(n)]

# 방향 순서: 오른쪽, 아래, 왼쪽, 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c, d = 0, 0, 0       # 왼쪽 위에서 시작, 처음 방향은 오른쪽
grid[r][c] = 'A'

for i in range(1, n * m):
    nr, nc = r + dr[d], c + dc[d]   # 지금 방향으로 한 칸 앞

    # 격자를 벗어나거나 이미 채운 칸이면 방향을 바꿈
    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != '':
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc
    grid[r][c] = chr(ord('A') + i % 26)

for row in grid:
    print(*row)