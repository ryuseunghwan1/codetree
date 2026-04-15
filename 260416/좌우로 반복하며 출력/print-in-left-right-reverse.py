N = int(input())


for i in range(1, N+1):
    if i % 2 == 0:
        for j in range(N, 0 , -1):
            print(j, end='')
        print()
    else:
        for m in range(1, N+1):
            print(m, end='')
        print()
    