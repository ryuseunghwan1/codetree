arr = [0] * 10
arr_1 = list(map(int, input().split()))

for j in arr_1:
    if j >= 100:
        arr[j // 10 -1] += 1
    elif j >= 90:
        arr[j // 10 -1] += 1
    elif j >= 80:
        arr[j // 10 -1] += 1
    elif j >= 70:
        arr[j // 10 -1] += 1
    elif j >= 60:
        arr[j // 10 -1] += 1
    elif j >= 50:
        arr[j // 10 -1] += 1
    elif j >= 40:
        arr[j // 10 -1] += 1
    elif j >= 30:
        arr[j // 10 -1] += 1
    elif j >= 20:
        arr[j // 10 -1] += 1
    elif j >= 10:
        arr[j // 10 -1] += 1
    elif j ==0:
        break    

for i in range(9, -1, -1):
    print(f'{ (i+1)*10 } - {arr[i]}')