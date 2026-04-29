arr = []
cnt = 0
for _ in range(4):
    cnt_arr = list(map(int, input().split()))
    arr.append(cnt_arr)

for i in range(4):
    for j in range(4):
        if j <= i:
            cnt += arr[i][j]
            
    