arr = list(map(int, input().split()))
arr_1 = []

for i in arr:
    if i != 0:
        arr_1.append(i)      
    else:
        break

print(sum(arr_1), round(sum(arr_1)/len(arr_1),1))