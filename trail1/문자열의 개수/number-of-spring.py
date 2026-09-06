
total = []
cnt = 0

while True:
    n = input()

    if n = '0':
        break
    else:
        total.append(n)
        cnt += 1
        
print(cnt)

for i in range(len(total)):
    if i % 2 == 0:
        print(total[i])
