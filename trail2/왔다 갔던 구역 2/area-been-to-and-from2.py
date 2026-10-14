OFFSET = 1000
MAX_R = 2000

n = int(input())
cnt = [0] * (MAX_R + 1)
cur = OFFSET  # 시작 위치 0

for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'R':
        for i in range(cur, cur + x):        # cur ~ cur+x-1 구간
            cnt[i] += 1
        cur += x
    else:  # 'L'
        for i in range(cur - x, cur):        # cur-x ~ cur-1 구간
            cnt[i] += 1
        cur -= x

print(sum(1 for c in cnt if c >= 2))


n = int(input())
cnt = [0] * (MAX_R + 1)
print(sum())