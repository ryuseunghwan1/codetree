import sys

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

count = sys.maxsize
for i in a:
    if i < count:
        count = i

print(count, a.count(count))
