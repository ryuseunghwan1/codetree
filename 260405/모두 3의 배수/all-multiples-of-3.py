cnt = 0
for i in range(5):
    N = int(input())

    if N % 3 ==0:
        cnt += 1

if cnt == 5:
    print(1)
else:
    print(0)

