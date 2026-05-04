a = input()
b = ''
c = ''

for i in list(a):
    if i.isalnum() == True:
        b += i

for j in list(b):
    if j.isalpha() == True:
        c += j.lower()
    else:
        c += j

print(c)