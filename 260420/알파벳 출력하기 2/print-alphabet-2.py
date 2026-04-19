N = int(input())

cnt = 0

for i in range(N):
    for j in range(i):
        print(' ', end=' ')
    for m in range(N-i):
        print(chr(65+cnt), end=' ')
        cnt += 1

        if cnt == 26:
            cnt = 0
    print()