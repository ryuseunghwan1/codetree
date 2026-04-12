N = int(input())

num = N-1

for i in range(1, N+1):
    print(' ' * num + '* ' * i)
    num -= 1

for j in range(1, N+1):
    print(' ' * j + '* ' * (N-j))