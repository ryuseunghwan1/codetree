start, end = map(int, input().split())
result = 0
# Please write your code here.
for i in range(start, end+1):
    total = 0
   
    for j in range(1,i+1):
        if i % j == 0:
            total += 1

    if total == 3:
        result += 1

print(result)
