n = int(input())

for i in range(1, n+1):
    cnt = 0
    for _ in range(n):
        
        print(i + cnt, end = ' ')
        cnt += n
    print()