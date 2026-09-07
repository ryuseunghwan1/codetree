a = input()
b = input()
c = ''
d = ''
for i in a:
    if i <= '9' and i >= '0':
        c += i

for j in b:
    if j <= '9' and j >= '0':
        d += j

print(int(c) + int(d))      