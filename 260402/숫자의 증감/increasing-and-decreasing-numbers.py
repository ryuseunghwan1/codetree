a, b = input().split()

if a == 'A':
    for i in range(1, int(b)+1):
        print(i, end=" ")
        
else:
    for j in range(int(b), 0, -1):
        print(j, end= " ")