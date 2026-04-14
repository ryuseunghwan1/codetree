N = int(input())

even = 1
odd = N

for i in range(N * 2):
    if i % 2 == 0:
        for j in range(even):
            print('*', end=' ')
        print()
        even += 1
    else:
        for n in range(odd):
            print('*', end=' ')
        print()
        odd -= 1    
        
    