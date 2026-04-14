N = int(input())

even = N
odd = 1

for i in range(N * 2):
    if i % 2 ==0:
        for j in range(even):
            print('*', end=' ')
        print()
        even -= 1
    else:
        for m in range(odd):
            print('*', end =' ')
        print()
        odd += 1
    
