a, b = map(int, input().split())

# Please write your code here.

def compare(a, b):
    if a == min(a,b):
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10

    return a, b

for i in compare(a,b):
    print(i, end=' ')