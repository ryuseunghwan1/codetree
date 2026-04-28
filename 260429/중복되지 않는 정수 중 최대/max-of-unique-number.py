n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
b = set(nums)

if len(nums) % len(b) != 0:
    print(max(b))
else:
    print(-1)