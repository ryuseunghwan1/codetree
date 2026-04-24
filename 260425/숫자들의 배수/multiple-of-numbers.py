N = int(input())
cnt = 0
cnt_1 = 0
while True:

    cnt += N
    print(cnt, end=' ')
    
    if cnt % 5 ==0:
        cnt_1 += 1

    if cnt_1 == 2:
        break
        