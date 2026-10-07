import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a_moves = [tuple(map(int, input().split())) for _ in range(n)]
b_moves = [tuple(map(int, input().split())) for _ in range(m)]

# 위치, 현재 처리 중인 이동 인덱스, 그 이동에서 남은 시간
pos_a = pos_b = 0
ia = ib = 0
rem_a = a_moves[0][1]   # 첫 이동의 남은 시간
rem_b = b_moves[0][1]

count = 0
prev_sign = 0   # 직전 선두 상태: 1=A앞, -1=B앞, 0=공동(아직 안 갈림)

while ia < n and ib < m:
    # 두 사람 중 더 빨리 끝나는 구간 길이만큼만 진행
    dt = min(rem_a, rem_b)

    # 그 시간만큼 이동
    pos_a += a_moves[ia][0] * dt
    pos_b += b_moves[ib][0] * dt
    rem_a -= dt
    rem_b -= dt

    # 현재 선두 판정
    if pos_a > pos_b:
        sign = 1
    elif pos_a < pos_b:
        sign = -1
    else:
        sign = 0   # 공동 선두

    # 선두가 '갈렸고', 직전과 다른 사람이 앞서면 → 선두 교체
    # 공동(0)은 "아직 안 바뀐 것"으로 보므로, 이전의 명확한 선두와만 비교
    if sign != 0 and prev_sign != 0 and sign != prev_sign:
        count += 1

    # prev_sign은 '명확한 선두'가 있었을 때만 갱신
    if sign != 0:
        prev_sign = sign

    # 다 쓴 이동은 다음 이동으로 넘김
    if rem_a == 0:
        ia += 1
        if ia < n:
            rem_a = a_moves[ia][1]
    if rem_b == 0:
        ib += 1
        if ib < m:
            rem_b = b_moves[ib][1]

print(count)