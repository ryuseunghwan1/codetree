n = int(input())

# Please write your code here.

def temp(n):

    if n == 0:
        return

    temp(n - 1)
    print(n, end=' ')

def temp_1(n):

    if n == 0:
        return

    print(n, end= ' ')
    temp_1(n-1)

temp(n)
print()
temp_1(n)