n = int(input())

# Please write your code here.

def star(n):

    if n == 0:
        return

    for i in range(n):
        print('*', end=' ')
    print()
    star(n -1)
    for j in range(n):
        print('*', end=' ')
    print()

star(n)