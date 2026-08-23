

n = int(input())

def f(n):

    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    return f(n-2) + n

print(f(n))