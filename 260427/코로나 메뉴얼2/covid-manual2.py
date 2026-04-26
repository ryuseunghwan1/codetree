arr = [(),(),()]
abcd = [0]*4

for i in range(3):
    a, b = input().split()
    arr[i] = (a,b)

for a , b in arr:
    if a == 'Y' and int(b) >= 37:
        abcd[0] += 1
    elif a == 'N' and int(b) >= 37:
        abcd[1] += 1
    elif a == 'Y' and int(b) < 37:
        abcd[2] += 1
    else:
        abcd[3] += 1

for i in abcd:
    print(i, end=' ')
    
if abcd[0] >= 2:
    print('E')
    