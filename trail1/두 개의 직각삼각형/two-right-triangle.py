N = int(input())

cnt_1 = N
cnt_2 = 0


for i in range(N):

    for j in range(cnt_1):
        print('*', end='')


    for m in range(cnt_2):
        print(' ', end='')

    for e in range(cnt_1):
        print('*', end='')

    print()
    
    cnt_1 -= 1
    cnt_2 += 2