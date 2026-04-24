a, b = map(int, input().split())

arr = [a, b]
for i in range(8):
    arr.append((arr[i] + arr[i+1]) % 10)

for j in arr:
    print(j, end=' ')