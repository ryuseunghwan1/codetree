a = list(input().split())
b = list(input().split())
c = list(input().split())

result = [a, b, c]
emergency = 0

for a, b in result:
    if a == 'Y' and int(b) >= 37:
        emergency += 1

if emergency >= 2:
    print('E')
else:
    print('N')