arr = list(map(int, input().split()))
even = 0
arr_2 = []
for i in arr[1::2]:
    even += i

for j in arr:
    if j % 3 ==0:
        arr_2.append(j)

print(even, round(sum(arr_2)/len(arr_2),1))