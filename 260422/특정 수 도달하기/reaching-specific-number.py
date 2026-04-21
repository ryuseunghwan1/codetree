N = list(map(int, input().split()))

cnt = 0
cnt_1 = 0
for i in N:
    if i >= 250:
        break
    else:
        cnt += i
        cnt_1 += 1

print(cnt, round(cnt/cnt_1,1))