N = int(input())

cnt_2 = N * 2 - 1

for i in range(N):
    for j in range(i):
        print(' ', end=' ')
    
    for e in range(cnt_2):
        print('*', end=' ')

    print()
    cnt_2 -= 2