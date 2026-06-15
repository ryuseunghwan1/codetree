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
        return False

calcul_list = ['+', '-', '/', '*']

if o in calcul_list:
    print(a, o, c, '=', calcul(a,o,c))
else:
    print(False)
    
