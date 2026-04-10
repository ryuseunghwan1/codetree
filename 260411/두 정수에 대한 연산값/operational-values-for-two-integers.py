a, b = map(int, input().split())

# Please write your code here.

def maxi(a, b):
    if a == max(a,b):
        a = a + 25
        b = b * 2
    else:
        a *= 2
        b += 25
    return a, b

for i in maxi(a, b):
    print(i, end= ' ')