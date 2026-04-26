a, b = map(int, input().split())
arr = [0]* 10
total = 0

while a > 0:
    cnt = a % 4
    arr[cnt] += 1
    a = a // 4
    
for i in arr:
    total += i ** 2
    
print(total)