
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i > count:
        count = i
print(count)