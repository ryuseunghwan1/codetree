N = int(input())
arr = [1, N]

for i in range(10):
    cnt = arr[-1]
    if cnt < 100:
        arr.append(arr[i] + arr[i+1])
    else:
        break

for j in arr:
    print(j, end=' ')
