N = int(input())

for i in range(N):
    num = 0
    num_1, num_2 = map(int, input().split())

    for j in range(num_1, num_2+1):
        if j % 2==0:
            num += j
    print(num)
    