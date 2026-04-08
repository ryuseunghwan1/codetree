a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calcul(a,o,c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '/':
        return int(a/c)
    elif o == '*':
        return a * c
    else:
        False

print(a, o, c, '=', calcul(a,o,c))
    
