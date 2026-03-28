num1, num2 = map(int, input().split())

while num1 >= 0:
    
    print(num1, end=" ")
    if num1 % 2 == 0:
        num1 += 3 
    else:
        num1 *= 2
        
    if num1 >= num2:
        print(num2)
        break
    
