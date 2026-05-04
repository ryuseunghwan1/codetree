a = list(input())

while len(a)>1:
    n = int(input())

    if n < len(a):
        a.pop(n)
        print(('').join(a))
    else:
        a.pop()
        print(('').join(a))


