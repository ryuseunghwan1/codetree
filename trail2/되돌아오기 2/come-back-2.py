cmds = input().strip()

# 북(0)에서 시작. dx, dy를 북동남서 순으로
# 북: (0,1), 동: (1,0), 남: (0,-1), 서: (-1,0)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 0          # 0:북 1:동 2:남 3:서
time = 0
answer = -1

for cmd in cmds:
    time += 1                      # 모든 명령은 1초 소모
    if cmd == 'R':
        d = (d + 1) % 4            # 오른쪽 = 시계방향
    elif cmd == 'L':
        d = (d - 1) % 4            # 왼쪽 = 반시계방향
    else:  # 'F'
        x += dx[d]
        y += dy[d]

    # 명령 처리 후 원점에 처음 도달하면 기록하고 종료
    if x == 0 and y == 0:
        answer = time
        break

print(answer)