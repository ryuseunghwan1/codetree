N = int(input())
cnt = N
cnt_1 = 0
while True:
    print(cnt, end=' ')
    cnt += N

    if cnt % 5 ==0:
        cnt_1 += 1

    if cnt_1 == 2:
        print(cnt)
        break
        