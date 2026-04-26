a, b = map(int, input().split())
arr = [0]* 10
total = 0

while a > 1:
    cnt = a % b
    arr[cnt] += 1
    a = a // b
    print(cnt)
    
for i in arr:
    total += i ** 2
    
print(total)