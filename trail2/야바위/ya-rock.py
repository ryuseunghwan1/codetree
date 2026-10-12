n = int(input())
ops = [tuple(map(int, input().split())) for _ in range(n)]

best = 0
for start in (1, 2, 3):
    pos = start
    score = 0
    for a, b, c in ops:
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
        if pos == c:
            score += 1
    best = max(bes, score)

print(best)