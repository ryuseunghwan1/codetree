arr = list(map(int, input().split()))
arr_1 = []

for i in arr:
    if i != 0:
        arr_1.append(i)      
    else:
        break

for j in arr_1[::-1]:
    print(j, end= ' ')