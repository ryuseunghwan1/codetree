n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
arr = arr[1:]
arr.sort()
for i in arr:
    print(i, end=' ')