import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def expand(k):
    """k번의 이동을 1초 단위 위치 변화(+1/-1) 리스트로 펼침"""
    steps = []
    for _ in range(k):
        cnt, d = input().split()
        cnt = int(cnt)
        delta = -1 if d == 'L' else 1   # L: 왼쪽(-), R: 오른쪽(+)
        steps.extend([delta] * cnt)
    return steps

a_steps = expand(n)
b_steps = expand(m)

# 둘 중 더 오래 움직이는 시간까지 시뮬레이션
total_time = max(len(a_steps), len(b_steps))

pos_a = pos_b = 0      # 시작 위치(같음)
count = 0
prev_same = True       # 0초엔 같은 위치 (이건 카운트 대상 아님)

for t in range(total_time):
    # 아직 움직일 스텝이 남았으면 이동, 끝났으면 제자리
    if t < len(a_steps):
        pos_a += a_steps[t]
    if t < len(b_steps):
        pos_b += b_steps[t]

    same = (pos_a == pos_b)

    # 직전엔 달랐는데(prev_same=False) 지금 같아졌으면 → 만남
    if same and not prev_same:
        count += 1

    prev_same = same

print(count)