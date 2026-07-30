x, y = map(int, input().split())

cnt = 0
for i in range(x, y+1):
    a, b = tuple(map(int, list(str(i))))
    result = a + b
    cnt = max(cnt, result)

print(cnt)