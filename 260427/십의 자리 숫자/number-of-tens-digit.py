arr = [0] * 9
arr_1 = list(map(int, input().split()))

for j in arr_1:
    if j >= 10:
        arr[j // 10 -1] += 1
    elif j ==0:
        break    

for i in range(9):
    print(f'{i+1} - {arr[i]}')