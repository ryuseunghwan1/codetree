n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
cnt_1 = 0
arr_1 = []

for i in arr:
    cnt += 1
    arr_1.append(i)
    if cnt % 2 != 0:
        print(arr_1[cnt_1], end=' ')
        cnt_1 += 1
    
    