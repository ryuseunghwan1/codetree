num = int(input())
temp = 0

for i in range(1, num+1):
    
    if not (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        temp += 1
    else:
        temp += 0

print(temp)