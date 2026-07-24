a = input().split()
b = a[0]
c = a[1]

d = []
e = []

for i in b:
    try:
        d.append(int(i))
    except:
        break
        
for j in c:
    try: 
        e.append(int(j))
    except:
        break

f = ''
g = ''
for m in d:
    f += str(m)
for n in e:
    g += str(n)

print(int(f) + int(g))
    