N = int(input())

cnt = 1
for i in range(N):
    for _ in range(N):
        print(cnt, end=' ')
        cnt += 1
    print()