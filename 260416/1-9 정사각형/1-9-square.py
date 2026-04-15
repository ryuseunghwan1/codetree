N = int(input())

cnt = 1

if cnt < 10:
    for i in range(N):
        for j in range(N):
            if cnt < 10:
                print(cnt, end='')
                cnt += 1
            else:
                cnt = 1
                print(cnt, end='')
                cnt += 1
        print()
