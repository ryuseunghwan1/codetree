num1 = int(input())
num2 = list(map(int, input().split()))

for i in num2[::-1]:
   if i % 2 ==0:
       print(i, end=" ")