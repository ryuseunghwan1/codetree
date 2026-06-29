n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 방향별 이동량 (행 변화, 열 변화)
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
# 벽에 부딪혔을 때 뒤집히는 방향
flip = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

time = 0
while time < t:
    dr, dc = move[d]
    nr, nc = r + dr, c + dc

    # 다음 칸이 벽 바깥이면 → 방향 전환 (1초 소모, 위치는 그대로)
    if nr < 1 or nr > n or nc < 1 or nc > n:
        d = flip[d]
    else:
        r, c = nr, nc   # 정상 이동
    time += 1

print(r, c)