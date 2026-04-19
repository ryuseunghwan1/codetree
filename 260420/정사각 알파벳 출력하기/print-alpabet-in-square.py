N = int(input())

for i in range(1, N*N+1):
    if i % N == 0:
        print(chr(64+i))
    else:
        print(chr(64+i), end='')