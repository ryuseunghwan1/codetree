a, b = map(int, input().split())
n = input()

# Please write your code here.
digits = []
num = 0
for i in range(len(n)):
    num = num * a + int(n[i])

while True:
    if num < b:
        digits.append(num % b)
        break
    
    digits.append(num % b)
    num //= b

for j in digits[::-1]:
    print(j, end='')