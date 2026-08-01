n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
possible = False

for i in range(n):
    remaining = segments[:i] + segments[i+1:]

    max_x1 = max(seg[0] for seg in remaining)

    min_x2 = min(seg[1] for seg in remaining)

    if max_x1 <= min_x2:
        possible = True
        break

if possible:
    print('Yes')
else:
    print('No')