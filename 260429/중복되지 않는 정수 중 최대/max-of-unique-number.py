n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
b = []

for i in nums:
    if nums.count(i) == 1:
        b.append(i)

if len(b) >0:
    print(max(b))
else:
    print(-1)