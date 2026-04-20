N = int(input())

for _ in range(N):
    NN = int(input())
    cnt = NN
    cnt_1 = 0

    while True:
        if cnt == 1:
            break
        if cnt % 2==0:
            cnt = cnt // 2
            cnt_1 += 1
        else:
            cnt = cnt * 3 + 1
            cnt_1 += 1

    print(cnt_1)