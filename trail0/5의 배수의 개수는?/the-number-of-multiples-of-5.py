matrix = [list(map(int,input().split())) for _ in range(4)]
count = 0
for i in matrix:
    for j in i:
        if j % 5 == 0:
            count += 1
print(count)

