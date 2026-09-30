N = int(input())
N_1 = list(map(float, input().split()))

cnt = 0
cnt_1 = 0
for i in N_1:
    cnt += i
    cnt_1 += 1

if cnt/cnt_1 >= 4.0:
    print(round(cnt/cnt_1,1))
    print('Perfect')
elif cnt/cnt_1 >= 3.0:
    print(round(cnt/cnt_1,1))
    print('Good')
else:
    print(round(cnt/cnt_1,1))
    print('Poor')