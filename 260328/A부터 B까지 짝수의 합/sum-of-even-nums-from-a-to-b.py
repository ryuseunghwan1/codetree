num1, num2 = map(int, input().split())
count = 0
for i in range(num1, num2+1):
    if i % 2 ==0:
        count += i

print(count)