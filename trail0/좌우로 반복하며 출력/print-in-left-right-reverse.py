num = int(input())
cnt = 1
row = []


for i in range(num):
    row.append(cnt)
    cnt += 1


for j in range(num):
    if j % 2 == 0:
        for i in range(num):
            print(row[i], end="")
    else:
        for i in range(num-1, -1, -1):
            print(row[i], end= "")
    print()