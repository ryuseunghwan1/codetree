N, B = map(int, input().split())

# Please write your code here.

digits = []

if B == 4:
    while True:
        if N < 4:
            digits.append(N % 4)
            break

        digits.append(N % 4)
        N //= 4
else:
    while True:
        if N < 4:
            digits.append(N % 8)
            break

        digits.append(N % 8)
        N //= 8

for i in digits[::-1]:
    print(i, end='')
            