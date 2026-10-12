n = int(input())
ops = [tuple(map(int, input().split())) for _ in range(n)]

best = 0
for start in (1, 2, 3):      # 조약돌을 1번, 2번, 3번 자리에 두는 경우를 각각 시도
    pos = start              # 조약돌이 지금 있는 자리
    score = 0
    for a, b, c in ops:
        if pos == a:         # 조약돌이 든 컵이 a번 자리에 있으면 b번 자리로 이동
            pos = b
        elif pos == b:       # b번 자리에 있으면 a번 자리로 이동
            pos = a
        if pos == c:         # 열어 본 자리에 조약돌이 있으면 1점
            score += 1
    best = max(best, score)

print(best)