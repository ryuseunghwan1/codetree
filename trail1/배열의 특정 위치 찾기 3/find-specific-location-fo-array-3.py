arr = list(map(int, input().split()))
arr_tmp = []
cnt = 0

for i in arr:
    if i != 0:
        arr_tmp.append(i)
    else:
        break

for j in range(3):
    cnt += arr_tmp[::-1][j]

print(cnt)
    
