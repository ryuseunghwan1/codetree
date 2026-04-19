N = int(input())

for i in range(N):
    print('  ' * i, end='' )

    for j in range(N-i, 0, -1):
        print(j, end=' ')
    print()
        