

x, y = map(int, input().split())

cnt = 0
for i in range(x, y + 1):
    result = sum(map(int, list(str(i))))
    cnt = max(cnt, result)

print(cnt)