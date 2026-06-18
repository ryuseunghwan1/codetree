n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = arr[0]
cnt = 1

for i in ragne(1, n):
    if min_val > arr[i]:
        min_val = arr[i]
        cnt = 1
    elif min_val == arr[i]:
        cnt += 1


print(min_val, cnt)