n = int(input())

# Please write your code here.

def temp(n):
    
    if n == 0:
        return
    
    temp(n-1)
    print('HelloWorld')

temp(n)