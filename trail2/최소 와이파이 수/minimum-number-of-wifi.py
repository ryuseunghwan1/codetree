n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cover = 2 * m + 1
print(len(arr) // cover)
