n = int(input())

space = n-1
star = 1
for i in range(n):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2


for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))    
    