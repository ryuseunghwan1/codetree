matrix = [list(map(int,input().split())) for _ in range(4)]

a = 0
b = 0
c= 0
d =0

for i in range(4):
    for j in range(4):
        if i == 0:
            a += matrix[i][j]
        elif i == 1:
            b += matrix[i][j]
        elif i == 2:
            c += matrix[i][j]
        else:
            d += matrix[i][j]

print(a)
print(b)
print(c)
print(a)