a, b = map(int, input().split())



for i in range(a, b-1, -2):
    if i % 2 ==0:
        continue
    else:
        print(i, end='')