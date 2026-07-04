a, b = map(int, input().split())
arr = []
arr.append(a)
arr.append(b)

for a in range(2, 10, 1):
    s = arr[a-2] + arr[a-1]
    if s >= 10:
        n = s % 10
        arr.append(n)
    else:
        arr.append(s)

print(*arr)