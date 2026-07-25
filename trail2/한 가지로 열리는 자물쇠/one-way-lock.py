n = int(input())
a, b, c = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for m in range(1, n + 1):
            # 세 자리 중 단 한 자리라도 거리가 2 이내인 경우
            if abs(i - a) <= 2 or abs(j - b) <= 2 or abs(m - c) <= 2:
                cnt += 1

print(cnt)