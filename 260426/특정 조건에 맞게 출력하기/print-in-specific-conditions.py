arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i != 0:
        cnt += 1
    else:
        break

for j in arr[:cnt]:
    if j % 2 ==0:
        print(j // 2, end=' ')
    else:
        print(j + 3, end=' ')