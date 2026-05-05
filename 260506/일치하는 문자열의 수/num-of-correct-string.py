a = input().split()
cnt = 0

for i in range(int(a[0])):
    b = input()

    if b == a[1]:
        cnt += 1

print(cnt)