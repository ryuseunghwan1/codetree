a, b = map(str, input().split())
c, d = ord(a), ord(b)

if c>d:
    print(c + d, c-d)
else:
    print(c + d, d-c)