arr = list(map(int, input().split()))

cnt =0
for i in arr:
    if i % 3 !=0:
        cnt += 1
    else:
        break

print(arr[cnt-1])
        