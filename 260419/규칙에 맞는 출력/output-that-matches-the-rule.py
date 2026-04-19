N = int(input())

cnt = N

for i in range(N):
    for j in range(i, -1, -1):
        print(N - j, end=' ')
    print()