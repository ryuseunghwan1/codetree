string = input()
invert = []
for i in string[1::2]:
    invert.append(i)

for j in invert[::-1]:
    print(j, end='')
    