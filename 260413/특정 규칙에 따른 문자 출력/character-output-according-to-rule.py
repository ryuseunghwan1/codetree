N = int(input())

num = N-1

for i in range(1, N):
    print('  ' * num + '@ ' * i)
    num -= 1

    
for j in range(N, 0, -1):
    print('@ ' * j)
        