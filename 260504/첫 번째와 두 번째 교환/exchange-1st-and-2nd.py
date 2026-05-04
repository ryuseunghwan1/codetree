a = list(input())
b = []

for i in a:
    if i == a[0]:
        b.append(a[1])
    elif i == a[1]:
        b.append(a[0])
    else:
        b.append(i)

c = ('').join(b)
print(c)