a = input()
b = list(input())

for i in b:
    if i == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)
