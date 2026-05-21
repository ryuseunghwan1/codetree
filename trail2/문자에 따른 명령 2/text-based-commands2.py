# 명령 문자열 입력받기
commands = input()

# 현재 위치 초기화
x, y = 0, 0

# 북(0), 동(1), 남(2), 서(3) 순서로 dx, dy 배열 설정 (시계 방향)
# - 북쪽 이동: y가 1 증가
# - 동쪽 이동: x가 1 증가
# - 남쪽 이동: y가 1 감소
# - 서쪽 이동: x가 1 감소
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 처음에는 북쪽(0)을 바라보고 시작합니다.
dir_num = 0

# 명령을 하나씩 읽으며 처리
for cmd in commands:
    if cmd == 'L':
        # 왼쪽으로 90도 회전 (반시계 방향)
        dir_num = (dir_num - 1) % 4
    elif cmd == 'R':
        # 오른쪽으로 90도 회전 (시계 방향)
        dir_num = (dir_num + 1) % 4
    elif cmd == 'F':
        # 바라보고 있는 방향으로 한 칸 전진
        x += dx[dir_num]
        y += dy[dir_num]

# 최종 위치 출력
print(x, y)