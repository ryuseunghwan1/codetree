arr = list(map(int, input().split()))
arr_1 = []
arr_2 = []

for i in arr:
    if i != 0:
        arr_1.append(i)      
    else:
        break

for j in arr_1:
    if j % 2 == 0:
        arr_2.append(j)

print(len(arr_2), sum(arr_2))
