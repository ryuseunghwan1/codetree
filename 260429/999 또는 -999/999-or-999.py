arr = list(map(int, input().split()))
arr_1 = []
for i in arr:
    if (i == 999 or i == -999):
        break
    else:
        arr_1.append(i)

print(max(arr_1), min(arr_1))