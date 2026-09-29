n = int(input())

# 방향별 이동량 (N: 위, E: 오른쪽, S: 아래, W: 왼쪽)
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': 1, 'E': 0, 'S': -1, 'W': 0}

x, y = 0, 0
time = 0
answer = -1

for _ in range(n):
    d, dist = input().split()
    dist = int(dist)

    for _ in range(dist):          # 한 칸씩 이동
        x += dx[d]
        y += dy[d]
        time += 1

        if x == 0 and y == 0:      # 처음으로 원점에 돌아옴
            answer = time
            break

    if answer != -1:
        break

print(answer)