a, b = map(int, input().split())
arr = [0]* 10
total = 0

while a > 0:
    cnt = a % b
    arr[cnt] += 1
    a = a // b
    
for i in arr:
    total += i ** 2
    