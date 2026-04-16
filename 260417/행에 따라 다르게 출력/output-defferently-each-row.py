N = int(input())

cnt = 0

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            cnt += 1
            print(cnt, end=' ')
        else:
            cnt += 2
            print(cnt, end=' ')
    print()
    