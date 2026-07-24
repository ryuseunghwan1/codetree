a, b = map(int, input().split())
c = a + b
d = str(c)

cnt = 0

for i in d:
    if i == '1':
        cnt += 1

print(cnt)