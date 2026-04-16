N = int(input())

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            print(N * i + j + 1, end=' ')
        else:
            print(N * (1+i) - j, end=' ')
    print()