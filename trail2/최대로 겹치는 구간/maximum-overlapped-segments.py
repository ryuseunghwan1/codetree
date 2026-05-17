n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

cnt = [0 for _ in range(201)]


for a, b in segments:
    
    for i in range(100+a, 100+b+1):
        cnt[i] += 1

max(cnt)