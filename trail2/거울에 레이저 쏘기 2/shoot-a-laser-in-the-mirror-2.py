n = int(input())
grid = [input() for _ in range(n)]
k = int(input())

# 방향 번호: 0=위, 1=오른쪽, 2=아래, 3=왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 시작 위치와 방향 정하기 (왼쪽 위에서 시계 방향으로 1번 ~ 4N번)
if k <= n:              # 위쪽 변: 아래로 쏨
    r, c, d = 0, k - 1, 2
elif k <= 2 * n:        # 오른쪽 변: 왼쪽으로 쏨
    r, c, d = k - n - 1, n - 1, 3
elif k <= 3 * n:        # 아래쪽 변: 위로 쏨
    r, c, d = n - 1, 3 * n - k, 0
else:                   # 왼쪽 변: 오른쪽으로 쏨
    r, c, d = 4 * n - k, 0, 1

cnt = 0
while 0 <= r < n and 0 <= c < n:    # 격자 안에 있는 동안 반복
    if grid[r][c] == '/':
        d = d ^ 1       # 위<->오른쪽, 아래<->왼쪽
    else:
        d = 3 - d       # 위<->왼쪽, 오른쪽<->아래
    cnt += 1
    r += dr[d]
    c += dc[d]

print(cnt)