arr = list(map(int, input().split()))

find_zero = 0
result = 0
for i in arr:
    if i == 0:
        break
    else:
        find_zero += 1

for j in range(find_zero-1,find_zero-4,-1):
    result += arr[j]

print(result)
