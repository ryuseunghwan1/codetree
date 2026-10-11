n, m = map(int, input().split())

# 테두리 검사를 쉽게 하려고 격자를 한 칸씩 여유 있게 만듭니다 (1번~n번 칸 사용)
grid = [[0] * (n + 2) for _ in range(n + 2)]

# 위, 아래, 왼쪽, 오른쪽으로 한 칸 이동하는 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(m):
    r, c = map(int, input().split())
    grid[r][c] = 1  # 색칠

    cnt = 0
    for i in range(4):
        cnt += grid[r + dr[i]][c + dc[i]]  # 인접한 칸이 칠해져 있으면 1이 더해짐

    print(1 if cnt == 3 else 0)