n = int(input())
arr = list(map(int, input().split()))
total = []

for a in range(n-1, 0 , -1):
    total.append(arr[a] - arr[a-1])

print(min(total))