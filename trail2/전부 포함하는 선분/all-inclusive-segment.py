n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = float('inf')

for i in range(n):
    # 1. i번째 사람만 빼고 나머지를 모은다
    others = []
    for j in range(n):
        if j != i:
            others.append(segments[j])

    # 2. 나머지 중 가장 왼쪽, 가장 오른쪽 찾기
    left = min(a for a, b in others)
    right = max(b for a, b in others)

    # 3. 사진 폭 계산, 가장 좁은 것 기록
    ans = min(ans, right - left)

