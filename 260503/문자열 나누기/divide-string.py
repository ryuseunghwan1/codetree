n = int(input())
cnt = input().split()

b = ''.join(cnt)

for i in range(len(b)):
    print(b[i], end='')
    if (i + 1) % 5 == 0:
        print()