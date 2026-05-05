a = input()
for i in list(a):
    if i <= 'Z' and i >= 'A':
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')