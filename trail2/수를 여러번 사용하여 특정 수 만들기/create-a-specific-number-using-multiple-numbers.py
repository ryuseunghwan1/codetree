A, B, C = map(int, input().split())

# Please write your code here.

big, small = max(A, B), min(A, B)

ans = 0
for y in range(C // big + 1):
    rest = C - big * y
    ans = max(ans, big * y + (rest // small) * small)

print(ans)