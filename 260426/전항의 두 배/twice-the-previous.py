a, b = map(int, input().split())
arr = [a, b]
for i in range(8):
    arr.append(arr[i+1] + 2 * arr[i])

for j in arr:
    print(j, end = ' ')
