N = int(input())
cnt = N
for i in range(N*2-1):
    for j in range(cnt):
        print('*', end = ' ')
    print()
    
    if i < N-1:
        cnt -= 1
    else:
        cnt += 1