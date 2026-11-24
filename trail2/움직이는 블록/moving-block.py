n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
for i in blocks:
    if i > sum(blocks) // len(blocks):
        ans += i - (sum(blocks) // len(blocks))

print(ans)