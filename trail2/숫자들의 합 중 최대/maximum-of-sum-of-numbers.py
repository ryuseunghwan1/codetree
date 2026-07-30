x, y = map(int, input().split())

cnt = 0
for i in range(x, y+1):
    a, b = tuple(map(int, list(str(i))))
    result = a + b
    cnt = max(cnt, result)

print(cnt)

x, y = map(int, input().split())

cnt = 0
for i in range(x, y + 1):
    s = str(i).zfill(2)  
    a, b = int(s[0]), int(s[1])

    result = a + b
    cnt = max(cnt, result)

print(cnt)