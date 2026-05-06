cnt = 0
total = []

while True:
    n = input()

    if n != '0':
        cnt += 1
        total.append(n)
    else:
        break

print(cnt)

for i in range(len(total)):
    if i % 2 == 0:
        print(total[i])