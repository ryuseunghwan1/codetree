arr = list(map(int, input().split()))

arr_1 = [0 for _ in range(6)]

for i in arr:
    arr_1[i-1] +=1

for j in range(1,7):
    print(f'{j} - {arr_1[j-1]}')
    
