N = int(input())

for i in range(1, N+1):
    cnt = 0
    for j in range(N+1-i, 0, -1):
        cnt += 1
        if j != 1:
            print(f'{i} * {cnt} = {i*cnt} /', end = " ")
        else:
            print(f'{i} * {cnt} = {i*cnt}')