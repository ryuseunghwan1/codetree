N = int(input())

for i in range(N * 2 + 1):
    for m in range(N * 2 + 1):
        if i == 0 or m % 2 == 0 or m == 0 or i % 2 == 0:
            print('*', end= ' ')
        else:
            print(' ', end=' ')
    print()