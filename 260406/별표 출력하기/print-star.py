N = int(input())
cnt = 0

for i in range(N):
    for j in range(i + 1):
        print('*', end=' ')
    print()
    cnt +=1


for i in range(N-1):
    for j in range(cnt-1):
        print('*', end=' ')
    print()
    cnt -=1
