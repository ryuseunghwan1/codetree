n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
arr.sort()
for i in arr:
    print(i, end=' ')