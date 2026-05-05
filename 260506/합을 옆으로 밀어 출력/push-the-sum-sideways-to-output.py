num = int(input())
cnt = 0
for i in range(num):
    n = int(input())

    cnt += n

a = str(cnt)
b = a[1:] + a[0]
print(b)