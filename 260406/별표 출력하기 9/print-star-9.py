N = int(input())
cnt = 1
for i in range(1, N+1):

    for j in range(N-i):
        print(' ', end=' ')

    for e in range(cnt):
        print('*', end=' ')

    print()
    cnt += 2